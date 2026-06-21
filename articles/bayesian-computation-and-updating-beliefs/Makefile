.PHONY: all python r calculators
all: python r calculators
python:
	python3 python/bayesian_computation_updating_beliefs_audit.py
r:
	Rscript r/bayesian_computation_updating_beliefs_summary.R
calculators:
	bash calculators/run_calculator_smoke_tests.sh
