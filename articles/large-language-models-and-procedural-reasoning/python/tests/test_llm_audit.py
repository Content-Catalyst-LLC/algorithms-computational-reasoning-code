from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "large_language_models_procedural_reasoning_audit.py"
spec = importlib.util.spec_from_file_location("llm_audit", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
assert spec.loader is not None
spec.loader.exec_module(module)


class LLMAuditTests(unittest.TestCase):
    def test_step_counter(self):
        self.assertEqual(module.count_steps("Step 1: A. Step 2: B. Step 3: C."), 3)

    def test_source_extraction(self):
        self.assertEqual(module.extract_sources("Claim [source:a] and [source:b]."), {"a", "b"})

    def test_high_stakes_overclaim_escalates(self):
        config = module.LLMAuditConfig()
        row = {
            "case_id": "x",
            "task": "high stakes",
            "output": "This is guaranteed and always correct.",
            "expected_sources": "source:z",
            "stakes": "high",
            "requires_factual_support": 1,
            "tool_used": "none",
        }
        result = module.audit_output(row, config)
        self.assertEqual(result["status"], "escalate")
        self.assertIn("guaranteed", result["risk_flags"])

    def test_grounded_procedure_passes(self):
        config = module.LLMAuditConfig()
        row = {
            "case_id": "y",
            "task": "sourced summary",
            "output": "Step 1: scope. Step 2: evidence. Step 3: conclusion [source:a].",
            "expected_sources": "source:a",
            "stakes": "medium",
            "requires_factual_support": 1,
            "tool_used": "retrieval",
        }
        result = module.audit_output(row, config)
        self.assertEqual(result["status"], "pass")


if __name__ == "__main__":
    unittest.main()
