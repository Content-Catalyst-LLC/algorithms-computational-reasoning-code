.PHONY: all python r calculators optional clean

all: python r calculators

python:
	python3 python/security_failures_as_algorithmic_failures_audit.py

r:
	Rscript r/security_failures_as_algorithmic_failures_summary.R

calculators:
	python3 calculators/python/security_failure_calculator.py
	Rscript calculators/r/security_failure_calculator.R

optional:
	@echo "Optional language examples are run directly by the populate script when toolchains are available."

clean:
	rm -rf outputs/tables/* outputs/json/* outputs/figures/* calculators/outputs/*
