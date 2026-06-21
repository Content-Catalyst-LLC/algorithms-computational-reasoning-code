PYTHON ?= python3
ARTICLE_DIR := .
PY_SCRIPT := python/automated_reasoning_symbolic_ai_hybrid_systems_audit.py
TEST_SCRIPT := python/test_symbolic_reasoning.py

.PHONY: run test calculators r clean all

all: run test calculators r

run:
	$(PYTHON) $(PY_SCRIPT)

test:
	$(PYTHON) $(TEST_SCRIPT)

calculators:
	bash calculators/run_calculator_smoke_tests.sh

r:
	@if command -v Rscript >/dev/null 2>&1; then Rscript r/automated_reasoning_symbolic_ai_hybrid_systems_summary.R; else echo "Rscript not found; skipping R diagnostics."; fi

clean:
	rm -rf outputs/tables/*.csv outputs/json/*.json outputs/figures/*.png outputs/logs/*.log calculators/outputs/*
	find . -type d -name '__pycache__' -prune -exec rm -rf {} +
