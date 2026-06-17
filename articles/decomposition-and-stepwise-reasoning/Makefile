.PHONY: all smoke python test calculator r julia sql haskell rust go c cpp fortran java typescript prolog racket clean

all: python test calculator r julia sql haskell rust go c cpp fortran java typescript prolog racket
smoke: python calculator sql

python:
	@if command -v python3 >/dev/null 2>&1; then PYTHONPATH=python python3 python/decomposition_audit/cli.py; else echo "python3 not found; skipping."; fi

test:
	@if command -v python3 >/dev/null 2>&1 && python3 -c "import pytest" >/dev/null 2>&1; then PYTHONPATH=python python3 -m pytest python/tests; else echo "pytest not found; skipping tests."; fi

calculator:
	@if command -v python3 >/dev/null 2>&1; then python3 python/calculators/decomposition_score_calculator.py --output-dir outputs/json; else echo "python3 not found; skipping calculator."; fi

r:
	@if command -v Rscript >/dev/null 2>&1; then Rscript r/decomposition_summary.R; else echo "Rscript not found; skipping."; fi

julia:
	@if command -v julia >/dev/null 2>&1; then mkdir -p outputs/tables && julia julia/decomposition_simulation.jl > outputs/tables/julia_decomposition_cases.csv; else echo "julia not found; skipping."; fi

sql:
	@if command -v sqlite3 >/dev/null 2>&1; then mkdir -p outputs/tables && sqlite3 outputs/tables/decomposition_cases.sqlite < sql/schema.sql && sqlite3 outputs/tables/decomposition_cases.sqlite < sql/analysis_queries.sql > outputs/tables/sql_decomposition_report.txt; else echo "sqlite3 not found; skipping."; fi

haskell:
	@$(MAKE) -C haskell run

rust:
	@if command -v cargo >/dev/null 2>&1; then cd rust && cargo run --quiet > ../outputs/tables/rust_decomposition_cases.csv; else echo "cargo not found; skipping."; fi

go:
	@if command -v go >/dev/null 2>&1; then cd go && go run main.go > ../outputs/tables/go_decomposition_cases.csv; else echo "go not found; skipping."; fi

c:
	@if command -v cc >/dev/null 2>&1; then cc -O2 -std=c11 c/decomposition_audit.c -o outputs/decomposition_audit_c && ./outputs/decomposition_audit_c > outputs/tables/c_decomposition_audit.csv; else echo "cc not found; skipping."; fi

cpp:
	@$(MAKE) -C cpp run

fortran:
	@if command -v gfortran >/dev/null 2>&1; then gfortran -O2 fortran/decomposition_model.f90 -o outputs/decomposition_model_fortran && ./outputs/decomposition_model_fortran > outputs/tables/fortran_decomposition_model.txt; else echo "gfortran not found; skipping."; fi

java:
	@if command -v javac >/dev/null 2>&1 && command -v java >/dev/null 2>&1; then mkdir -p outputs/java_classes outputs/tables && javac -d outputs/java_classes java/src/main/java/org/contentcatalyst/algorithms/DecompositionAudit.java && java -cp outputs/java_classes org.contentcatalyst.algorithms.DecompositionAudit > outputs/tables/java_decomposition_audit.csv; else echo "Java toolchain not found; skipping."; fi

typescript:
	@if command -v npx >/dev/null 2>&1; then cd typescript && npx tsc --noEmit || true; else echo "npx not found; skipping TypeScript."; fi

prolog:
	@if command -v swipl >/dev/null 2>&1; then swipl -q -s prolog/decomposition_rules.pl -g "decomposition_score('Scientific simulation', S), writeln(S), halt." > outputs/tables/prolog_decomposition_rules.txt; else echo "swipl not found; skipping."; fi

racket:
	@if command -v racket >/dev/null 2>&1; then racket racket/recursive_decomposition_interpreter.rkt > outputs/tables/racket_recursive_decomposition_interpreter.csv; else echo "racket not found; skipping."; fi

clean:
	rm -rf outputs/tables/* outputs/figures/* outputs/json/* outputs/logs/* outputs/reports/* outputs/java_classes outputs/decomposition_audit_c outputs/decomposition_model_fortran
	$(MAKE) -C haskell clean || true
	$(MAKE) -C cpp clean || true
	cd rust && cargo clean || true
