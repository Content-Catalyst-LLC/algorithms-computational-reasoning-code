PYTHON ?= python3
R_SCRIPT ?= Rscript

.PHONY: run test r calculators clean all

all: run test calculators

run:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) python/overfitting_underfitting_model_error_audit.py | tee outputs/logs/python_workflow.log

test: run
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m unittest discover -s tests -p 'test_*.py'

r: run
	@if command -v $(R_SCRIPT) >/dev/null 2>&1; then \
		$(R_SCRIPT) r/overfitting_underfitting_model_error_summary.R | tee outputs/logs/r_workflow.log; \
	else \
		echo "Rscript not available; skipping R diagnostics." | tee outputs/logs/r_workflow.log; \
	fi

calculators:
	bash calculators/run_calculator_smoke_tests.sh | tee outputs/logs/calculator_smoke_tests.log

clean:
	rm -rf outputs/tables/* outputs/json/* outputs/figures/* outputs/logs/* calculators/outputs/*
	find . -type d -name '__pycache__' -prune -exec rm -rf {} +
