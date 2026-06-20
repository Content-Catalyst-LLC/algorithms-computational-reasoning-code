.PHONY: all python r calculators clean

all: python calculators

python:
	python3 python/multi_objective_tradeoff/audit.py
	python3 python/multi_objective_tradeoff/cli.py

r:
	Rscript r/multi_objective_optimization_tradeoff_summary.R

calculators:
	python3 calculators/python/tradeoff_calculator.py

clean:
	rm -rf outputs/tables/* outputs/json/* outputs/figures/* outputs/cli/* calculators/outputs/*
