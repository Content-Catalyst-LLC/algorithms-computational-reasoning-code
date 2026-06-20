.PHONY: all python r calculators optional clean

all: python r calculators

python:
	python3 python/authentication_authorization_identity_audit.py

r:
	Rscript r/authentication_authorization_identity_summary.R

calculators:
	python3 calculators/python/identity_access_calculator.py
	Rscript calculators/r/identity_access_calculator.R

optional:
	@echo "Optional language examples are run directly by the populate script when toolchains are available."

clean:
	rm -rf outputs/tables/* outputs/json/* outputs/figures/* calculators/outputs/*
