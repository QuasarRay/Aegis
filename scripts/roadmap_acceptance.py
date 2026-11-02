"""Fixed source-host acceptance producers used by materialized Aegis recipes."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "infra"))
from agentinfra.atomic import atomic_write_json
from agentinfra.roadmap_inventory import authority_inventory, reconcile_inventory, save_inventory
from agentinfra.roadmap_records import digest, file_binding
from agentinfra.security import confined_path


HOST_EXCLUSIONS = {
    "test_atomic_transaction.TestAtomicWrite.test_atomic_write_accepts_lexical_alias_of_same_resolved_root":
        "host exposes no distinct lexical alias for the current workspace",
    "test_locks.TestProcessLock.test_transient_permission_error_during_create_is_bounded_contention":
        "Windows sharing violations are a Windows host behavior",
}


def flatten(suite):
    for test in suite:
        if isinstance(test, unittest.TestSuite):
            yield from flatten(test)
        else:
            yield test


class RecordedResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.occurrences = {}

    def startTest(self, test):
        self.occurrences[test.id()] = {"id": test.id(), "outcome": "STARTED"}
        super().startTest(test)

    def addSuccess(self, test):
        self.occurrences[test.id()]["outcome"] = "PASS"
        super().addSuccess(test)

    def addFailure(self, test, err):
        self.occurrences.setdefault(test.id(), {"id": test.id()})["outcome"] = "FAIL"
        super().addFailure(test, err)

    def addError(self, test, err):
        self.occurrences.setdefault(test.id(), {"id": test.id()})["outcome"] = "ERROR"
        super().addError(test, err)

    def addSkip(self, test, reason):
        self.occurrences.setdefault(test.id(), {"id": test.id()}).update(outcome="SKIP", reason=reason,
                    host_exclusion=HOST_EXCLUSIONS.get(test.id()) == reason)
        super().addSkip(test, reason)

    def addSubTest(self, test, subtest, err):
        self.occurrences[test.id()].setdefault("subtests", []).append({"id": str(subtest), "outcome": "PASS" if err is None else "FAIL"})
        if err is not None:
            self.occurrences[test.id()]["outcome"] = "FAIL"
        super().addSubTest(test, subtest, err)

    def addExpectedFailure(self, test, err):
        self.occurrences[test.id()]["outcome"] = "EXPECTED_FAILURE"
        super().addExpectedFailure(test, err)

    def addUnexpectedSuccess(self, test):
        self.occurrences[test.id()]["outcome"] = "UNEXPECTED_SUCCESS"
        super().addUnexpectedSuccess(test)


def tests(candidate: str) -> dict:
    suite = unittest.defaultTestLoader.discover(str(ROOT / "infra/tests"), pattern="test*.py")
    expected = [test.id() for test in flatten(suite)]
    sources = [file_binding(ROOT, p.relative_to(ROOT).as_posix()) for p in sorted((ROOT / "infra/tests").rglob("*.py"))]
    result = unittest.TextTestRunner(verbosity=2, resultclass=RecordedResult).run(suite)
    occurrences = list(result.occurrences.values())
    modules = [file_binding(ROOT, str(Path(module.__file__).resolve().relative_to(ROOT)))
               for name, module in sorted(sys.modules.copy().items())
               if (name == "agentinfra" or name.startswith("agentinfra.")) and getattr(module, "__file__", None)]
    accepted = (bool(expected) and len(expected) == len(set(expected)) and set(expected) == set(result.occurrences) and
                result.wasSuccessful() and all(row["outcome"] == "PASS" or
                row["outcome"] == "SKIP" and row.get("host_exclusion") for row in occurrences))
    return {"schema": 1, "kind": "complete_source_host_original_tests", "candidate": candidate,
            "required": expected, "source_files": sources, "occurrences": occurrences, "accepted": accepted,
            "loaded_modules": modules, "loaded_identity": digest(modules), "domain_proof": False,
            "installed_artifact_acceptance": False, "platform": sys.platform}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["tests", "source"])
    parser.add_argument("--output", required=True)
    parser.add_argument("--candidate", required=True)
    args = parser.parse_args()
    if args.action == "tests":
        record = tests(args.candidate)
    else:
        snapshot = authority_inventory(ROOT, remote=True)
        reconciliation = reconcile_inventory(ROOT, snapshot)
        saved = save_inventory(ROOT, snapshot)
        record = {"schema": 1, "kind": "complete_source_reconciliation", "candidate": args.candidate,
                  "reconciliation": reconciliation, "snapshot": saved, "inventory_digest": snapshot["digest"],
                  "accepted": reconciliation["status"] == "RECONCILED", "domain_proof": False}
    atomic_write_json(confined_path(ROOT, args.output), record, root=ROOT, mode=0o600)
    print({"candidate": args.candidate, "accepted": record["accepted"], "domain_proof": False})
    return 0 if record["accepted"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
