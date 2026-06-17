.PHONY: all smoke python test calculator r julia sql haskell rust go c cpp fortran java typescript prolog racket clean

all: python test calculator r julia sql haskell rust go c cpp fortran java typescript prolog racket
smoke: python calculator sql

python:
	@if command -v python3 >/dev/null 2>&1; then PYTHONPATH=python python3 python/execution_models/cli.py; else echo "python3 not found; skipping."; fi

test:
	@if command -v python3 >/dev/null 2>&1 && python3 -c "import pytest" >/dev/null 2>&1; then PYTHONPATH=python python3 -m pytest python/tests; else echo "pytest not found; skipping tests."; fi

calculator:
	@if command -v python3 >/dev/null 2>&1; then PYTHONPATH=python python3 python/calculators/execution_quality_calculator.py --output-dir outputs/json && PYTHONPATH=python python3 python/calculators/build_reproducibility_calculator.py --output-dir outputs/json; else echo "python3 not found; skipping calculator."; fi

r:
	@if command -v Rscript >/dev/null 2>&1; then Rscript r/execution_model_summary.R; else echo "Rscript not found; skipping."; fi

julia:
	@if command -v julia >/dev/null 2>&1; then mkdir -p outputs/tables && julia julia/interpreter_examples.jl > outputs/tables/julia_tiny_interpreter.csv; else echo "julia not found; skipping."; fi

sql:
	@if command -v sqlite3 >/dev/null 2>&1; then mkdir -p outputs/tables && sqlite3 outputs/tables/execution_model_cases.sqlite < sql/schema.sql && sqlite3 outputs/tables/execution_model_cases.sqlite < sql/analysis_queries.sql > outputs/tables/sql_execution_model_report.txt; else echo "sqlite3 not found; skipping."; fi

haskell:
	@$(MAKE) -C haskell run

rust:
	@if command -v cargo >/dev/null 2>&1; then cd rust && cargo run --quiet > ../outputs/tables/rust_tiny_interpreter.csv; else echo "cargo not found; skipping."; fi

go:
	@if command -v go >/dev/null 2>&1; then cd go && go run main.go > ../outputs/tables/go_tiny_interpreter.csv; else echo "go not found; skipping."; fi

c:
	@if command -v cc >/dev/null 2>&1; then cc -O2 -std=c11 c/execution_model_audit.c -o outputs/execution_model_audit_c && ./outputs/execution_model_audit_c > outputs/tables/c_execution_model_audit.csv; else echo "cc not found; skipping."; fi

cpp:
	@$(MAKE) -C cpp run

fortran:
	@if command -v gfortran >/dev/null 2>&1; then gfortran -O2 fortran/execution_quality_model.f90 -o outputs/execution_quality_model_fortran && ./outputs/execution_quality_model_fortran > outputs/tables/fortran_execution_quality_model.txt; else echo "gfortran not found; skipping."; fi

java:
	@if command -v javac >/dev/null 2>&1 && command -v java >/dev/null 2>&1; then mkdir -p outputs/java_classes outputs/tables && javac -d outputs/java_classes java/src/main/java/org/contentcatalyst/algorithms/ExecutionModelAudit.java && java -cp outputs/java_classes org.contentcatalyst.algorithms.ExecutionModelAudit > outputs/tables/java_tiny_interpreter.csv; else echo "Java toolchain not found; skipping."; fi

typescript:
	@if command -v tsc >/dev/null 2>&1; then cd typescript && tsc --noEmit || true; else echo "tsc not found; skipping TypeScript without network install."; fi

prolog:
	@if command -v swipl >/dev/null 2>&1; then swipl -q -s prolog/execution_model_rules.pl -g "execution_quality(X, Y), write(X), write(','), writeln(Y), fail; halt." > outputs/tables/prolog_execution_model_rules.txt; else echo "swipl not found; skipping."; fi

racket:
	@if command -v racket >/dev/null 2>&1; then racket racket/tiny_interpreter.rkt > outputs/tables/racket_tiny_interpreter.csv; else echo "racket not found; skipping."; fi

clean:
	rm -rf outputs/tables/* outputs/figures/* outputs/json/* outputs/logs/* outputs/reports/* outputs/java_classes outputs/execution_model_audit_c outputs/execution_quality_model_fortran
	$(MAKE) -C haskell clean || true
	$(MAKE) -C cpp clean || true
	cd rust && cargo clean || true
