.PHONY: all python r calculators clean
all: python calculators
python:
	python3 python/algorithmic_game_theory/audit.py
	python3 python/algorithmic_game_theory/cli.py
r:
	Rscript r/algorithmic_game_theory_strategic_behavior_summary.R
calculators:
	python3 calculators/python/strategic_behavior_calculator.py
clean:
	rm -rf outputs/tables/* outputs/json/* outputs/figures/* outputs/cli/* calculators/outputs/*
