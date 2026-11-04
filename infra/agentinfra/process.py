from __future__ import annotations

from dataclasses import dataclass
from contextlib import contextmanager
from contextvars import ContextVar
from datetime import datetime, timezone
import hashlib
import ctypes
import ctypes.wintypes
import os
import signal
import subprocess
import tempfile
import threading
import time
import uuid
from pathlib import Path
from typing import Callable, Iterable, Mapping

from .security import minimal_subprocess_env, redact_text


_process_observer = ContextVar("aegis_process_observer", default=None)
_recipe_group = ContextVar("aegis_recipe_process_group", default=None)


@contextmanager
def observe_process(callback: Callable[[subprocess.Popen], None]):
    """Observe the existing supervisor's child without introducing another owner."""
    token = _process_observer.set(callback)
    try:
        yield
    finally:
        _process_observer.reset(token)


if os.name == "nt":
    class _IO_COUNTERS(ctypes.Structure):
        _fields_ = [
            ("ReadOperationCount", ctypes.c_ulonglong),
            ("WriteOperationCount", ctypes.c_ulonglong),
            ("OtherOperationCount", ctypes.c_ulonglong),
            ("ReadTransferCount", ctypes.c_ulonglong),
            ("WriteTransferCount", ctypes.c_ulonglong),
            ("OtherTransferCount", ctypes.c_ulonglong),
        ]


    class _JOBOBJECT_BASIC_LIMIT_INFORMATION(ctypes.Structure):
        _fields_ = [
            ("PerProcessUserTimeLimit", ctypes.c_longlong),
            ("PerJobUserTimeLimit", ctypes.c_longlong),
            ("LimitFlags", ctypes.wintypes.DWORD),
            ("MinimumWorkingSetSize", ctypes.c_size_t),
            ("MaximumWorkingSetSize", ctypes.c_size_t),
            ("ActiveProcessLimit", ctypes.wintypes.DWORD),
            ("Affinity", ctypes.c_size_t),
            ("PriorityClass", ctypes.wintypes.DWORD),
            ("SchedulingClass", ctypes.wintypes.DWORD),
        ]


    class _JOBOBJECT_EXTENDED_LIMIT_INFORMATION(ctypes.Structure):
        _fields_ = [
            ("BasicLimitInformation", _JOBOBJECT_BASIC_LIMIT_INFORMATION),
            ("IoInfo", _IO_COUNTERS),
            ("ProcessMemoryLimit", ctypes.c_size_t),
            ("JobMemoryLimit", ctypes.c_size_t),
            ("PeakProcessMemoryUsed", ctypes.c_size_t),
            ("PeakJobMemoryUsed", ctypes.c_size_t),
        ]


def _assign_kill_job(proc: subprocess.Popen):
    if os.name != "nt":
        return None
    kernel = ctypes.windll.kernel32
    kernel.CreateJobObjectW.restype = ctypes.wintypes.HANDLE
    kernel.CreateJobObjectW.argtypes = (ctypes.c_void_p, ctypes.wintypes.LPCWSTR)
    kernel.SetInformationJobObject.argtypes = (ctypes.wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, ctypes.wintypes.DWORD)
    kernel.AssignProcessToJobObject.argtypes = (ctypes.wintypes.HANDLE, ctypes.wintypes.HANDLE)
    kernel.CloseHandle.argtypes = (ctypes.wintypes.HANDLE,)
    kernel.TerminateJobObject.argtypes = (ctypes.wintypes.HANDLE, ctypes.wintypes.UINT)
    job = kernel.CreateJobObjectW(None, None)
    if not job:
        return None
    info = _JOBOBJECT_EXTENDED_LIMIT_INFORMATION()
    info.BasicLimitInformation.LimitFlags = 0x00002000  # JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
    if not kernel.SetInformationJobObject(job, 9, ctypes.byref(info), ctypes.sizeof(info)):
        kernel.CloseHandle(job)
        return None
    if not kernel.AssignProcessToJobObject(job, ctypes.wintypes.HANDLE(int(proc._handle))):
        kernel.CloseHandle(job)
        return None
    return job


def _close_job(job) -> None:
    if job is not None and os.name == "nt":
        ctypes.windll.kernel32.CloseHandle(job)


@dataclass(frozen=True)
class ProcessResult:
    argv: tuple[str, ...]
    cwd: str
    returncode: int
    stdout: str
    stderr: str
    stdout_sha256: str
    stderr_sha256: str
    stdout_bytes: int
    stderr_bytes: int
    stdout_truncated: bool
    stderr_truncated: bool
    timed_out: bool
    started_at: str
    finished_at: str
    duration_seconds: float
    stdout_path: str | None = None
    stderr_path: str | None = None


class _Capture:
    def __init__(self, limit: int, archive: Path | None = None):
        self.limit = limit
        self.buffer = bytearray()
        self.digest = hashlib.sha256()
        self.size = 0
        self.archive = archive
        self.error = None

    def consume(self, stream) -> None:
        output = None
        try:
            if self.archive is not None:
                fd = os.open(self.archive, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
                output = os.fdopen(fd, "wb")
            while True:
                chunk = stream.read(65536)
                if not chunk:
                    return
                self.digest.update(chunk)
                self.size += len(chunk)
                if output is not None:
                    output.write(chunk)
                if len(self.buffer) < self.limit:
                    self.buffer.extend(chunk[: self.limit - len(self.buffer)])
        except BaseException as exc:
            self.error = exc
            # Keep draining after archive failure; a full pipe must not deadlock
            # the child. The owner rejects this incomplete capture below.
            while stream.read(65536):
                pass
        finally:
            if output is not None:
                try:
                    output.close()
                except BaseException as exc:
                    self.error = exc

    def text(self) -> str:
        return redact_text(bytes(self.buffer).decode("utf-8", "replace"))


def _kill_tree(proc: subprocess.Popen, job=None, *, group: int | None = None) -> None:
    if proc.poll() is not None:
        if job is not None and os.name == "nt":
            ctypes.windll.kernel32.TerminateJobObject(job, 1)
        return
    if os.name == "nt":
        if job is not None and ctypes.windll.kernel32.TerminateJobObject(job, 1):
            return
        subprocess.run(
            ["taskkill", "/PID", str(proc.pid), "/T", "/F"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
            env=minimal_subprocess_env(),
        )
        if proc.poll() is None:
            proc.kill()
    else:
        try:
            os.killpg(group if group is not None else proc.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass


def run_recipe_stage(
    argv: Iterable[str],
    *,
    cwd: Path,
    timeout: float | None = 60.0,
    env: Mapping[str, str] | None = None,
    capture_limit: int = 1_000_000,
) -> ProcessResult:
    """Run a fixed stage under the outer recipe's existing POSIX group owner.

    A stage timeout kills the entire recipe group, including this process. The
    outer supervisor then records the outcome using its actual creation handle.
    Ordinary run_process callers retain their original version-one interface.
    """
    if os.name != "posix" or os.getsid(0) != os.getpid():
        raise ValueError("inherited process group requires an owned POSIX recipe session")
    token = _recipe_group.set(os.getpgrp())
    try:
        logs = cwd / ".aegis/roadmaps/stage-logs" / uuid.uuid4().hex if timeout is None else None
        return run_process(argv, cwd=cwd, timeout=timeout, env=env, capture_limit=capture_limit,
                           output_directory=logs)
    finally:
        _recipe_group.reset(token)


def run_process(
    argv: Iterable[str],
    *,
    cwd: Path,
    timeout: float | None = 60.0,
    env: Mapping[str, str] | None = None,
    capture_limit: int = 1_000_000,
    output_directory: Path | None = None,
) -> ProcessResult:
    # A fixed multi-stage recipe may keep all tools under the outer supervisor's
    # actual process-group handle. This is allowed only for a POSIX session
    # leader created by that supervisor. A stage timeout terminates that entire
    # owned recipe group, including this process; the outer owner records it.
    inherited_group = _recipe_group.get()
    command = tuple(argv)
    if not command or not all(isinstance(item, str) and item for item in command):
        raise ValueError("argv must be a non-empty sequence of non-empty strings")
    if timeout is not None and (timeout <= 0 or timeout != timeout or timeout == float("inf")):
        raise ValueError("timeout must be None (unlimited) or finite and positive")
    if capture_limit < 1024:
        raise ValueError("capture_limit must be at least 1024 bytes")
    if output_directory is not None:
        output_directory.mkdir(parents=True, exist_ok=True)
    stdout_path = output_directory / "stdout.raw" if output_directory is not None else None
    stderr_path = output_directory / "stderr.raw" if output_directory is not None else None
    started_wall = datetime.now(timezone.utc).isoformat()
    started = time.monotonic()
    flags = subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0
    with tempfile.TemporaryDirectory(prefix="aegis-process-home-") as isolated_directory:
        isolated_home = Path(isolated_directory)
        child_env = minimal_subprocess_env(env)
        defaults = {
            "HOME": str(isolated_home),
            "USERPROFILE": str(isolated_home),
            "HOMEDRIVE": isolated_home.drive or "",
            "HOMEPATH": str(isolated_home)[len(isolated_home.drive) :] if isolated_home.drive else str(isolated_home),
            "APPDATA": str(isolated_home / "AppData" / "Roaming"),
            "LOCALAPPDATA": str(isolated_home / "AppData" / "Local"),
            "XDG_CACHE_HOME": str(isolated_home / ".cache"),
            "XONSH_DATA_DIR": str(isolated_home / ".local" / "share" / "xonsh"),
            "XONSH_CACHE_DIR": str(isolated_home / ".cache" / "xonsh"),
        }
        for key, value in defaults.items():
            child_env.setdefault(key, value)
        for key in (
            "APPDATA",
            "LOCALAPPDATA",
            "XDG_CACHE_HOME",
            "XONSH_DATA_DIR",
            "XONSH_CACHE_DIR",
        ):
            Path(child_env[key]).mkdir(parents=True, exist_ok=True)
        proc = subprocess.Popen(
            command,
            cwd=cwd,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False,
            env=child_env,
            creationflags=flags,
            start_new_session=os.name != "nt" and inherited_group is None,
        )
        job = _assign_kill_job(proc)
        stdout_capture = _Capture(capture_limit, stdout_path)
        stderr_capture = _Capture(capture_limit, stderr_path)
        stdout_thread = threading.Thread(target=stdout_capture.consume, args=(proc.stdout,), daemon=True)
        stderr_thread = threading.Thread(target=stderr_capture.consume, args=(proc.stderr,), daemon=True)
        stdout_thread.start()
        stderr_thread.start()
        timed_out = False
        try:
            observer = _process_observer.get()
            if observer is not None:
                observer(proc)
            proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            _kill_tree(proc, job, group=inherited_group)
            proc.wait(timeout=10)
        except BaseException:
            _kill_tree(proc, job, group=inherited_group)
            proc.wait(timeout=10)
            raise
        finally:
            # Closing a kill-on-close job also removes descendants that kept
            # running after a normally exiting direct child.
            _close_job(job)
            job = None
            stdout_thread.join(timeout=10)
            stderr_thread.join(timeout=10)
            if stdout_thread.is_alive() or stderr_thread.is_alive():
                _kill_tree(proc, job, group=inherited_group)
                raise RuntimeError("subprocess output reader did not terminate")
            proc.stdout.close()
            proc.stderr.close()
        if stdout_capture.error or stderr_capture.error:
            raise RuntimeError("subprocess output archive failed") from (stdout_capture.error or stderr_capture.error)
        finished = time.monotonic()
        result = ProcessResult(
            argv=command,
            cwd=str(cwd.resolve()),
            returncode=int(proc.returncode),
            stdout=stdout_capture.text(),
            stderr=stderr_capture.text(),
            stdout_sha256=stdout_capture.digest.hexdigest(),
            stderr_sha256=stderr_capture.digest.hexdigest(),
            stdout_bytes=stdout_capture.size,
            stderr_bytes=stderr_capture.size,
            stdout_truncated=stdout_capture.size > capture_limit,
            stderr_truncated=stderr_capture.size > capture_limit,
            timed_out=timed_out,
            started_at=started_wall,
            finished_at=datetime.now(timezone.utc).isoformat(),
            duration_seconds=finished - started,
            stdout_path=str(stdout_path.resolve()) if stdout_path else None,
            stderr_path=str(stderr_path.resolve()) if stderr_path else None,
        )
    return result
