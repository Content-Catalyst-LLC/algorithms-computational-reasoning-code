.PHONY: all run test calculators r clean

all: run test calculators r

run:
	python3 python/supervised_unsupervised_rl_audit.py

test: run
	python3 python/test_learning_paradigms_workflow.py

calculators:
	bash calculators/run_calculator_smoke_tests.sh

r: run
	@if command -v Rscript >/dev/null 2>&1; then Rscript r/learning_paradigms_summary.R; else echo "Rscript not found; skipping R diagnostics."; fi

clean:
	rm -rf outputs/tables/* outputs/json/* outputs/figures/* outputs/logs/* calculators/outputs/*
