from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
JSON_DIR = ROOT / "outputs" / "json"


class ModelErrorOutputTests(unittest.TestCase):
    def test_summary_exists(self):
        path = JSON_DIR / "model_error_audit_summary.json"
        self.assertTrue(path.exists(), "missing model_error_audit_summary.json")
        payload = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(payload["article"], "overfitting_underfitting_and_model_error")
        self.assertGreaterEqual(payload["model_count"], 5)

    def test_complexity_metrics_have_expected_models(self):
        path = TABLES / "model_complexity_metrics.csv"
        rows = list(csv.DictReader(path.open(encoding="utf-8")))
        names = {row["model_name"] for row in rows}
        self.assertIn("constant_underfit", names)
        self.assertIn("high_degree_overfit", names)
        self.assertIn("regularized_high_degree", names)

    def test_moderate_model_beats_constant_on_test_error(self):
        path = TABLES / "model_complexity_metrics.csv"
        rows = {row["model_name"]: row for row in csv.DictReader(path.open(encoding="utf-8"))}
        self.assertLess(float(rows["moderate_polynomial"]["test_mse"]), float(rows["constant_underfit"]["test_mse"]))

    def test_validation_curve_written(self):
        path = TABLES / "model_error_validation_curve.csv"
        rows = list(csv.DictReader(path.open(encoding="utf-8")))
        self.assertEqual(len(rows), 13)


if __name__ == "__main__":
    unittest.main()
