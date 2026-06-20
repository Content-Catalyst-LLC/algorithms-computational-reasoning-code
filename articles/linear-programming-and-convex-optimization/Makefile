.PHONY: smoke all python r calculators test clean

smoke: python calculators

all: python r calculators test

python:
	python3 python/lp_convex/audit.py
	python3 python/lp_convex/cli.py

r:
	@if command -v Rscript >/dev/null 2>&1; then Rscript r/linear_programming_convex_optimization_summary.R; else echo "[WARN] Rscript unavailable; skipping R workflow."; fi

calculators:
	bash calculators/run_calculator_smoke_tests.sh

test:
	@if command -v pytest >/dev/null 2>&1; then pytest -q tests; else python3 tests/test_lp_convex.py; fi

clean:
	rm -rf outputs/tables/* outputs/json/* outputs/figures/* calculators/outputs/*
