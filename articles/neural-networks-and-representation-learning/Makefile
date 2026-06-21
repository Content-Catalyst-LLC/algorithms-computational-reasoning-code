.PHONY: run test calculator-smoke r clean

run:
	python3 python/neural_networks_representation_learning_audit.py
	@if command -v Rscript >/dev/null 2>&1; then Rscript r/neural_networks_representation_learning_summary.R; else echo "Rscript not found; skipping R diagnostics."; fi

test:
	python3 -m unittest discover -s python/tests -p 'test_*.py'

calculator-smoke:
	bash calculators/run_calculator_smoke_tests.sh

r:
	Rscript r/neural_networks_representation_learning_summary.R

clean:
	rm -rf outputs/tables/* outputs/json/* outputs/figures/* outputs/logs/* calculators/outputs/*
	find . -name '__pycache__' -type d -prune -exec rm -rf {} +
