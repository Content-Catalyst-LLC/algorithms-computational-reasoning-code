PYTHON ?= python3
R ?= Rscript

.PHONY: all smoke python r calculators clean

all: python calculators r

smoke:
	$(PYTHON) -m py_compile python/gradient_descent_ml/audit.py python/gradient_descent_ml/cli.py calculators/python/gradient_descent_calculator.py tests/smoke_test.py
	$(PYTHON) python/gradient_descent_ml/audit.py
	$(PYTHON) python/gradient_descent_ml/cli.py
	$(PYTHON) calculators/python/gradient_descent_calculator.py
	$(PYTHON) tests/smoke_test.py

python:
	$(PYTHON) python/gradient_descent_ml/audit.py
	$(PYTHON) python/gradient_descent_ml/cli.py

r:
	@if command -v $(R) >/dev/null 2>&1; then \
		$(R) r/gradient_descent_ml_optimization_summary.R; \
		$(R) calculators/r/gradient_descent_calculator.R; \
	else \
		echo "[WARN] Rscript not found; skipping R workflows."; \
	fi

calculators:
	$(PYTHON) calculators/python/gradient_descent_calculator.py

clean:
	rm -rf outputs/tables/* outputs/json/* outputs/figures/* calculators/outputs/*
