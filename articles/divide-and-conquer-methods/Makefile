.PHONY: all smoke python test calculator r julia sql haskell rust go c cpp fortran java typescript prolog racket clean
all: python test calculator r julia sql haskell rust go c cpp fortran java typescript prolog racket
smoke: python calculator sql
python:
	@if command -v python3 >/dev/null 2>&1; then PYTHONPATH=python python3 python/divide_conquer/cli.py; else echo "python3 not found; skipping."; fi
test:
	@if command -v python3 >/dev/null 2>&1 && python3 -c "import pytest" >/dev/null 2>&1; then PYTHONPATH=python python3 -m pytest python/tests; else echo "pytest not found; skipping tests."; fi
calculator:
	@if command -v python3 >/dev/null 2>&1; then PYTHONPATH=python python3 python/calculators/divide_conquer_quality_calculator.py --output-dir outputs/json && PYTHONPATH=python python3 python/calculators/recurrence_complexity_calculator.py --output-dir outputs/json; else echo "python3 not found; skipping calculator."; fi
r:
	@if command -v Rscript >/dev/null 2>&1; then Rscript r/divide_conquer_summary.R; else echo "Rscript not found; skipping."; fi
julia:
	@if command -v julia >/dev/null 2>&1; then mkdir -p outputs/tables && julia julia/divide_conquer_examples.jl > outputs/tables/julia_divide_conquer_examples.csv; else echo "julia not found; skipping."; fi
sql:
	@if command -v sqlite3 >/dev/null 2>&1; then mkdir -p outputs/tables && sqlite3 outputs/tables/divide_conquer_cases.sqlite < sql/schema.sql && sqlite3 outputs/tables/divide_conquer_cases.sqlite < sql/analysis_queries.sql > outputs/tables/sql_divide_conquer_report.txt; else echo "sqlite3 not found; skipping."; fi
haskell:
	@$(MAKE) -C haskell run
rust:
	@if command -v cargo >/dev/null 2>&1; then cd rust && cargo run --quiet > ../outputs/tables/rust_divide_conquer_checks.csv; else echo "cargo not found; skipping."; fi
go:
	@if command -v go >/dev/null 2>&1; then cd go && go run main.go > ../outputs/tables/go_divide_conquer_checks.csv; else echo "go not found; skipping."; fi
c:
	@if command -v cc >/dev/null 2>&1; then cc -O2 -std=c11 c/divide_conquer_audit.c -o outputs/divide_conquer_audit_c && ./outputs/divide_conquer_audit_c > outputs/tables/c_divide_conquer_checks.csv; else echo "cc not found; skipping."; fi
cpp:
	@$(MAKE) -C cpp run
fortran:
	@if command -v gfortran >/dev/null 2>&1; then gfortran -O2 fortran/divide_conquer_quality_model.f90 -o outputs/divide_conquer_quality_model_fortran && ./outputs/divide_conquer_quality_model_fortran > outputs/tables/fortran_divide_conquer_quality_model.txt; else echo "gfortran not found; skipping."; fi
java:
	@if command -v javac >/dev/null 2>&1 && command -v java >/dev/null 2>&1; then mkdir -p outputs/java_classes outputs/tables && javac -d outputs/java_classes java/src/main/java/org/contentcatalyst/algorithms/DivideConquerAudit.java && java -cp outputs/java_classes org.contentcatalyst.algorithms.DivideConquerAudit > outputs/tables/java_divide_conquer_checks.csv; else echo "Java toolchain not found; skipping."; fi
typescript:
	@if command -v tsc >/dev/null 2>&1; then cd typescript && tsc --noEmit || true; else echo "tsc not found; skipping TypeScript without network install."; fi
prolog:
	@if command -v swipl >/dev/null 2>&1; then swipl -q -s prolog/divide_conquer_rules.pl -g "recurrence(merge_sort,R),write('merge_sort,'),writeln(R),halt." > outputs/tables/prolog_divide_conquer_rules.txt; else echo "swipl not found; skipping."; fi
racket:
	@if command -v racket >/dev/null 2>&1; then racket racket/divide_conquer_checker.rkt > outputs/tables/racket_divide_conquer_checks.csv; else echo "racket not found; skipping."; fi
clean:
	rm -rf outputs/tables/* outputs/figures/* outputs/json/* outputs/logs/* outputs/reports/* outputs/java_classes outputs/divide_conquer_audit_c outputs/divide_conquer_quality_model_fortran
	$(MAKE) -C haskell clean || true
	$(MAKE) -C cpp clean || true
	cd rust && cargo clean || true
