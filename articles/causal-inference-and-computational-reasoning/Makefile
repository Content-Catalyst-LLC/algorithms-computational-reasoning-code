.PHONY: run python r test calculators clean tree

run: python calculators
	@echo "Completed core causal-inference workflow and calculators."

python:
	python3 python/causal_inference_audit_workflow.py
	python3 python/dag_adjustment_review.py
	python3 python/sensitivity_analysis.py

test:
	python3 python/tests/test_causal_workflow.py

calculators:
	bash calculators/run_calculator_smoke_tests.sh

r:
	Rscript r/causal_inference_diagnostics.R

clean:
	rm -f outputs/tables/*.csv outputs/json/*.json outputs/figures/*.png outputs/logs/*.json calculators/outputs/*

tree:
	find . -maxdepth 3 -type f | sort
