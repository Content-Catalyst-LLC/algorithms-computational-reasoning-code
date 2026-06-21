.PHONY: all python r calculators smoke clean

all: python calculators

python:
	python3 python/probabilistic_algorithms_reasoning_under_uncertainty_audit.py

r:
	Rscript r/probabilistic_algorithms_reasoning_under_uncertainty_summary.R

calculators:
	bash calculators/run_calculator_smoke_tests.sh

smoke: python calculators

clean:
	rm -rf outputs/tables/* outputs/json/* outputs/figures/* outputs/logs/* calculators/outputs/*
