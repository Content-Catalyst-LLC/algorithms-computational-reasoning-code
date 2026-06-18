.PHONY: all smoke python test calculator r julia sql haskell rust go c cpp fortran java typescript prolog racket clean
all: python test calculator r julia sql haskell rust go c cpp fortran java typescript prolog racket
smoke: python calculator sql
python:
	@if command -v python3 >/dev/null 2>&1; then PYTHONPATH=python python3 python/search_sorting/cli.py; else echo "python3 not found; skipping."; fi
test:
	@if command -v python3 >/dev/null 2>&1 && python3 -c "import pytest" >/dev/null 2>&1; then PYTHONPATH=python python3 -m pytest python/tests; else echo "pytest not found; skipping tests."; fi
calculator:
	@if command -v python3 >/dev/null 2>&1; then PYTHONPATH=python python3 python/calculators/search_sorting_quality_calculator.py --output-dir outputs/json && PYTHONPATH=python python3 python/calculators/search_complexity_calculator.py --output-dir outputs/json; else echo "python3 not found; skipping calculator."; fi
r:
	@if command -v Rscript >/dev/null 2>&1; then Rscript r/search_sorting_summary.R; else echo "Rscript not found; skipping."; fi
julia:
	@if command -v julia >/dev/null 2>&1; then mkdir -p outputs/tables && julia julia/search_sorting_examples.jl > outputs/tables/julia_search_sorting_examples.csv; else echo "julia not found; skipping."; fi
sql:
	@if command -v sqlite3 >/dev/null 2>&1; then mkdir -p outputs/tables && sqlite3 outputs/tables/search_sorting_cases.sqlite < sql/schema.sql && sqlite3 outputs/tables/search_sorting_cases.sqlite < sql/analysis_queries.sql > outputs/tables/sql_search_sorting_report.txt; else echo "sqlite3 not found; skipping."; fi
haskell:
	@$(MAKE) -C haskell run
rust:
	@if command -v cargo >/dev/null 2>&1; then cd rust && cargo run --quiet > ../outputs/tables/rust_search_sorting_checks.csv; else echo "cargo not found; skipping."; fi
go:
	@if command -v go >/dev/null 2>&1; then cd go && go run main.go > ../outputs/tables/go_search_sorting_checks.csv; else echo "go not found; skipping."; fi
c:
	@if command -v cc >/dev/null 2>&1; then cc -O2 -std=c11 c/search_sorting_audit.c -o outputs/search_sorting_audit_c && ./outputs/search_sorting_audit_c > outputs/tables/c_search_sorting_checks.csv; else echo "cc not found; skipping."; fi
cpp:
	@$(MAKE) -C cpp run
fortran:
	@if command -v gfortran >/dev/null 2>&1; then gfortran -O2 fortran/search_sorting_quality_model.f90 -o outputs/search_sorting_quality_model_fortran && ./outputs/search_sorting_quality_model_fortran > outputs/tables/fortran_search_sorting_quality_model.txt; else echo "gfortran not found; skipping."; fi
java:
	@if command -v javac >/dev/null 2>&1 && command -v java >/dev/null 2>&1; then mkdir -p outputs/java_classes outputs/tables && javac -d outputs/java_classes java/src/main/java/org/contentcatalyst/algorithms/SearchSortingAudit.java && java -cp outputs/java_classes org.contentcatalyst.algorithms.SearchSortingAudit > outputs/tables/java_search_sorting_checks.csv; else echo "Java toolchain not found; skipping."; fi
typescript:
	@if command -v tsc >/dev/null 2>&1; then cd typescript && tsc --noEmit || true; else echo "tsc not found; skipping TypeScript without network install."; fi
prolog:
	@if command -v swipl >/dev/null 2>&1; then swipl -q -s prolog/search_sorting_rules.pl -g "found(9,[7,2,9,1],I),write('linear_search_9,'),writeln(I),halt." > outputs/tables/prolog_search_sorting_rules.txt; else echo "swipl not found; skipping."; fi
racket:
	@if command -v racket >/dev/null 2>&1; then racket racket/search_sorting_checker.rkt > outputs/tables/racket_search_sorting_checks.csv; else echo "racket not found; skipping."; fi
clean:
	rm -rf outputs/tables/* outputs/figures/* outputs/json/* outputs/logs/* outputs/reports/* outputs/java_classes outputs/search_sorting_audit_c outputs/search_sorting_quality_model_fortran
	$(MAKE) -C haskell clean || true
	$(MAKE) -C cpp clean || true
	cd rust && cargo clean || true
