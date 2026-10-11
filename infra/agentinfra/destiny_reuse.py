"""Portable helpers reused verbatim from Aegis sibling branches.

See modules/destiny/reuse-provenance.json for source revisions and hashes.
MetaRocq authority, installation and roadmap assumptions are not imported.
"""


import hashlib
import json
import re


class ContractError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise ContractError(message)


def digest(value):
    data = value if isinstance(value, bytes) else json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def load_json(data):
    def unique(items):
        result = {}
        for k, v in items:
            require(k not in result, f"duplicate JSON key: {k}")
            result[k] = v
        return result
    return json.loads(data, object_pairs_hook=unique,
                      parse_constant=lambda s: require(False, f"non-finite JSON: {s}"))


def checked_output(o, result):
    if result.returncode or result.timed_out or result.stdout_truncated or result.stderr_truncated:
        return False
    out = result.stdout + "\n" + result.stderr
    if o["method"] == "kani":
        harnesses = re.findall(r"^Checking harness (.+?)\.\.\.$", out, re.M)
        statuses = re.findall(r"^\s*- Status: ([A-Z_]+)\s*$", out, re.M)
        return (harnesses == [o["entry"]] and out.count("VERIFICATION:- SUCCESSFUL") == 1
                and "SUCCESS" in statuses and set(statuses) <= {"SUCCESS", "SATISFIED"}
                and "VERIFICATION:- FAILED" not in out
                and "Complete - 1 successfully verified harnesses, 0 failures, 1 total." in out)
    summaries = re.findall(r"verification results::?\s*(\d+) verified, (\d+) errors", out)
    return summaries == [(str(o["expected_checks"]), "0")]
