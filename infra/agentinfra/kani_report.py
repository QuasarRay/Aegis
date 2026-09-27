"""Kani result inventory validation reused from QuasarRay/Candle-rs.

Source: tools/verify.py at 65ef925d106168f7d974e3ad4e4bfd5e5c3bb7c8.
The target repository's RPL-1.5 notice is retained in LICENSE.Candle-rs.
This reports bounded evidence only; it is not the shared HOL specification.
"""

def validate_kani_report(report, manifest):
    """Fail closed on incomplete execution, even if a tool exits successfully."""
    errors, harnesses = [], []
    expected = {f"proofs::{item['harness']}" for item in manifest["bounded_properties"]}
    if not expected:
        errors.append("No registered harnesses")
    try:
        if report["metadata"]["kani_version"] != manifest["kani_version"]:
            errors.append("Exported Kani version mismatch")
        results = report["verification_results"]["results"]
        identifiers = [item["harness_id"] for item in results]
        if len(identifiers) != len(set(identifiers)) or set(identifiers) != expected:
            errors.append("Executed harness inventory differs from the manifest")
        metadata = report["harness_metadata"]
        names = [item["pretty_name"] for item in metadata]
        if len(names) != len(set(names)) or set(names) != expected:
            errors.append("Harness metadata inventory differs from the manifest")
        for item in metadata:
            if item["attributes"]["kind"] != "Proof" or item["attributes"]["should_panic"]:
                errors.append(f"Unexpected proof attributes: {item['pretty_name']}")
        summary = report["verification_results"]["summary"]
        for key, value in {"total_harnesses": len(expected), "executed": len(expected),
                           "status": "completed", "successful": len(expected), "failed": 0}.items():
            if summary[key] != value:
                errors.append(f"Unexpected verification summary {key}: {summary[key]}")
        for item in results:
            checks = item["checks"]
            assertions = [check for check in checks if check["category"] == "assertion"
                          and check["function"] == item["harness_id"]
                          and check["status"] == "Success"]
            harnesses.append({"harness": item["harness_id"], "status": item["status"],
                              "duration_ms": item["duration_ms"],
                              "successful_harness_assertions": len(assertions)})
            if item["status"] != "Success" or not assertions:
                errors.append(f"No successful proof with reachable assertions: {item['harness_id']}")
            if any(check["status"] not in ("Success", "Unreachable") for check in checks):
                errors.append(f"Unresolved or failed check: {item['harness_id']}")
    except (KeyError, TypeError, ValueError) as error:
        errors.append(f"Malformed or unsupported Kani report: {error}")
    return {"passed": not errors, "errors": errors, "harnesses": harnesses}


