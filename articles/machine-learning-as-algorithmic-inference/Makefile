PYTHON ?= python3
R_SCRIPT ?= Rscript

.PHONY: all run test calculators r clean

all: run test calculators r

run:
	$(PYTHON) python/machine_learning_algorithmic_inference_audit.py

test:
	$(PYTHON) python/test_machine_learning_workflow.py

calculators:
	bash calculators/run_calculator_smoke_tests.sh

r:
	@if command -v $(R_SCRIPT) >/dev/null 2>&1; then \
		$(R_SCRIPT) r/machine_learning_algorithmic_inference_summary.R; \
	else \
		echo "Rscript not found; skipping optional R diagnostics."; \
	fi

clean:
	rm -f outputs/tables/*.csv outputs/json/*.json outputs/figures/*.png outputs/logs/*.log calculators/outputs/*
	find . -name '__pycache__' -type d -prune -exec rm -rf {} +
