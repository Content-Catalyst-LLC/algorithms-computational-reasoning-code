.PHONY: run python r test calculators clean tree

run: python calculators
	@echo "Completed core decision under uncertainty and computational risk workflow."

python:
	python3 python/decision_uncertainty_risk_workflow.py
	python3 python/risk_threshold_review.py
	python3 python/uncertainty_sensitivity_analysis.py

test:
	python3 python/tests/test_decision_risk_workflow.py

calculators:
	bash calculators/run_calculator_smoke_tests.sh

r:
	Rscript r/decision_risk_diagnostics.R

clean:
	rm -f outputs/tables/*.csv outputs/json/*.json outputs/figures/*.png outputs/logs/*.json calculators/outputs/*

tree:
	find . -maxdepth 3 -type f | sort
