PYTHON ?= python3
PY_SCRIPT := python/al_kindi_frequency_analysis_cryptanalysis_map.py
TEST_SCRIPT := python/test_cryptanalysis_map.py

.PHONY: all run test calculators r clean

all: run test calculators r

run:
	$(PYTHON) $(PY_SCRIPT)

test:
	$(PYTHON) $(TEST_SCRIPT)

calculators:
	bash calculators/run_calculator_smoke_tests.sh

r:
	@if command -v Rscript >/dev/null 2>&1; then Rscript r/al_kindi_frequency_analysis_cryptanalysis_summary.R; else echo "Rscript not found; skipping R diagnostics."; fi

clean:
	rm -rf outputs/tables/*.csv outputs/json/*.json outputs/figures/*.png outputs/logs/*.log calculators/outputs/*
	find . -type d -name '__pycache__' -prune -exec rm -rf {} +
