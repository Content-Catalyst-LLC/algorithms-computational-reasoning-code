from pathlib import Path
import csv
import importlib.util
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "python" / "training_testing_generalization_audit.py"
spec = importlib.util.spec_from_file_location("training_testing_generalization_audit", MODULE_PATH)
workflow = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = workflow
spec.loader.exec_module(workflow)

class TrainingTestingGeneralizationTests(unittest.TestCase):
    def test_sigmoid_range(self):
        self.assertGreater(workflow.sigmoid(0), 0)
        self.assertLess(workflow.sigmoid(0), 1)

    def test_generated_split_counts(self):
        config = workflow.default_config()
        rows = workflow.generate_dataset(config)
        self.assertEqual(len(rows), config.train_n + config.test_n + config.shifted_test_n)

    def test_model_evaluates(self):
        config = workflow.default_config()
        rows = workflow.generate_dataset(config)
        train = [row for row in rows if row["split"] == "train"]
        weights = workflow.fit_logistic(train, config)
        metrics = workflow.evaluate(train, weights, "train", config.threshold)
        self.assertGreaterEqual(metrics["accuracy"], 0)
        self.assertLessEqual(metrics["accuracy"], 1)

    def test_output_files_exist_after_run(self):
        workflow.main()
        expected = [
            ROOT / "outputs" / "tables" / "split_performance_metrics.csv",
            ROOT / "outputs" / "tables" / "cross_validation_metrics.csv",
            ROOT / "outputs" / "tables" / "generalization_risk_register.csv",
            ROOT / "outputs" / "json" / "training_testing_generalization_audit_summary.json",
        ]
        for path in expected:
            self.assertTrue(path.exists(), path)
        with (ROOT / "outputs" / "tables" / "split_performance_metrics.csv").open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual({row["split"] for row in rows}, {"train", "test", "shifted_test"})

if __name__ == "__main__":
    unittest.main()
