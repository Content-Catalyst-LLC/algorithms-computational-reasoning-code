.PHONY: run python r test calculators clean tree

run: python calculators
	@echo "Completed core causal algorithms and intervention modeling workflow."

python:
	python3 python/intervention_modeling_workflow.py
	python3 python/intervention_graph_review.py
	python3 python/intervention_policy_sensitivity.py

test:
	python3 python/tests/test_intervention_workflow.py

calculators:
	bash calculators/run_calculator_smoke_tests.sh

r:
	Rscript r/intervention_modeling_diagnostics.R

clean:
	rm -f outputs/tables/*.csv outputs/json/*.json outputs/figures/*.png outputs/logs/*.json calculators/outputs/*

tree:
	find . -maxdepth 3 -type f | sort
