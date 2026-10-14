"""Synthetic union tests; these establish no Destiny behavioral proof."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from agentinfra.coverage import assurance


class TestCaseConjunction(unittest.TestCase):
    def setUp(self):
        self.record = {"rust_translation_reviewed": True, "required_obligations": {
            "spec_proved": [{"entry": "proofs::a", "manifest": "verification/kani/Cargo.toml", "assertion_properties": ["a.assertion.1"]},
                            {"entry": "proofs::b", "manifest": "verification/kani/Cargo.toml", "assertion_properties": ["b.assertion.1", "b.assertion.2"]}],
            "production_rust_refinement_proved": [{"entry": "proofs::c", "manifest": "other/Cargo.toml", "assertion_properties": ["c.assertion.1"]}]}}

    def proof(self, entry, kind="spec_proved", manifest="verification/kani/Cargo.toml", status="CHECKED_SCOPED"):
        name = entry.split("::")[-1]
        return {"entry": entry, "assurance": kind, "manifest": manifest, "status": status,
                "assertion_properties": [f"{name}.assertion.1", f"{name}.assertion.2"]}

    def test_partial_assertion_list_does_not_discharge_a_whole_harness_requirement(self):
        proof = self.proof("proofs::b")
        proof["assertion_properties"] = ["b.assertion.1"]
        self.assertFalse(assurance(self.record, [self.proof("proofs::a"), proof])["spec_proved"])

    def test_one_success_does_not_discharge_two_assertion_obligations(self):
        self.assertFalse(assurance(self.record, [self.proof("proofs::a")])["spec_proved"])

    def test_proved_kernel_retains_unproved_wrapper_correspondence(self):
        proof = self.proof("proofs::c", kind="production_rust_refinement_proved", manifest="other/Cargo.toml")
        self.assertTrue(assurance(self.record, [proof])["production_rust_refinement_proved"])
        self.record["residual_correspondence"] = [{"lane": "production_rust_refinement_proved",
            "relation": "Native attachment and input conversion remain unproved"}]
        levels = assurance(self.record, [self.proof("proofs::a"), self.proof("proofs::b"), proof])
        self.assertTrue(levels["spec_proved"])
        self.assertFalse(levels["production_rust_refinement_proved"])
        self.assertTrue(assurance(self.record, [self.proof("proofs::a"), self.proof("proofs::b")])["spec_proved"])

    def test_stale_wrong_manifest_or_wrong_lane_does_not_discharge_requirement(self):
        for proof in (self.proof("proofs::b", status="STALE_SOURCE"),
                      self.proof("proofs::b", manifest="other/Cargo.toml"),
                      self.proof("proofs::b", kind="production_rust_refinement_proved")):
            self.assertFalse(assurance(self.record, [self.proof("proofs::a"), proof])["spec_proved"])

    def test_review_and_nonempty_requirements_are_required(self):
        self.assertFalse(any(assurance(None, [self.proof("proofs::a")]).values()))
        self.record["rust_translation_reviewed"] = False
        self.assertFalse(any(assurance(self.record, [self.proof("proofs::a"), self.proof("proofs::b")]).values()))
        self.record["rust_translation_reviewed"] = True
        self.record["required_obligations"]["spec_proved"] = []
        self.assertFalse(assurance(self.record, [self.proof("proofs::a")])["spec_proved"])

    def test_shared_helper_property_needs_its_exact_observed_location(self):
        helper="proofs::compare::<f64, 8>.assertion.1"
        self.record["required_obligations"]["spec_proved"][1]["assertion_properties"].append(helper)
        self.record["assertions"]=[{"rust_assertions":[{"entry":"proofs::b",
            "manifest":"verification/kani/Cargo.toml", "property":helper,
            "file":"verification/kani/src/helpers.rs", "line":7}]}]
        proof=self.proof("proofs::b")
        proof["assertion_properties"].append(helper)
        proofs=[self.proof("proofs::a"),proof]
        self.assertFalse(assurance(self.record,proofs)["spec_proved"])
        proof["assertion_locations"]={helper:{"file":"verification/kani/src/helpers.rs","line":7}}
        self.assertTrue(assurance(self.record,proofs)["spec_proved"])
        proof["assertion_locations"][helper]["line"]=8
        self.assertFalse(assurance(self.record,proofs)["spec_proved"])


if __name__ == "__main__":
    unittest.main()
