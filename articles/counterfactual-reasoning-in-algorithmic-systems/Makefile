.PHONY: run python r test calculators clean tree

run: python calculators
	@echo "Completed core counterfactual-reasoning workflow and calculators."

python:
	python3 python/counterfactual_reasoning_audit_workflow.py
	python3 python/counterfactual_threshold_review.py
	python3 python/recourse_feasibility_review.py

test:
	python3 python/tests/test_counterfactual_workflow.py

calculators:
	bash calculators/run_calculator_smoke_tests.sh

r:
	Rscript r/counterfactual_reasoning_diagnostics.R

clean:
	rm -f outputs/tables/*.csv outputs/json/*.json outputs/figures/*.png outputs/logs/*.json calculators/outputs/*

tree:
	find . -maxdepth 3 -type f | sort
