.PHONY: smoke all python r calculators

smoke: python calculators

all: python calculators r

python:
	python3 python/decision_classification/audit.py
	python3 python/decision_classification/cli.py --threshold 0.50

calculators:
	bash calculators/run_calculator_smoke_tests.sh

r:
	@if command -v Rscript >/dev/null 2>&1; then Rscript r/decision_rules_thresholds_classification_summary.R; else echo "[WARN] Rscript not available; skipping R workflow"; fi
