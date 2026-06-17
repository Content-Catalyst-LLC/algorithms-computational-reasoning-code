.PHONY: all smoke python test calculator r julia sql haskell rust go c cpp fortran java typescript prolog racket clean

all: python test calculator r julia sql haskell rust go c cpp fortran java typescript prolog racket
smoke: python calculator sql

python:
	@if command -v python3 >/dev/null 2>&1; then PYTHONPATH=python python3 python/tree_structures/cli.py; else echo "python3 not found; skipping."; fi

test:
	@if command -v python3 >/dev/null 2>&1 && python3 -c "import pytest" >/dev/null 2>&1; then PYTHONPATH=python python3 -m pytest python/tests; else echo "pytest not found; skipping tests."; fi

calculator:
	@if command -v python3 >/dev/null 2>&1; then python3 python/calculators/tree_structure_quality_calculator.py --output-dir outputs/json; else echo "python3 not found; skipping calculator."; fi

r:
	@if command -v Rscript >/dev/null 2>&1; then Rscript r/tree_structure_summary.R; else echo "Rscript not found; skipping."; fi

julia:
	@if command -v julia >/dev/null 2>&1; then mkdir -p outputs/tables && julia julia/tree_traversal_examples.jl > outputs/tables/julia_tree_structure_cases.csv; else echo "julia not found; skipping."; fi

sql:
	@if command -v sqlite3 >/dev/null 2>&1; then mkdir -p outputs/tables && sqlite3 outputs/tables/tree_structure_cases.sqlite < sql/schema.sql && sqlite3 outputs/tables/tree_structure_cases.sqlite < sql/analysis_queries.sql > outputs/tables/sql_tree_structure_report.txt; else echo "sqlite3 not found; skipping."; fi

haskell:
	@$(MAKE) -C haskell run

rust:
	@if command -v cargo >/dev/null 2>&1; then cd rust && cargo run --quiet > ../outputs/tables/rust_tree_structure_cases.csv; else echo "cargo not found; skipping."; fi

go:
	@if command -v go >/dev/null 2>&1; then cd go && go run main.go > ../outputs/tables/go_tree_structure_cases.csv; else echo "go not found; skipping."; fi

c:
	@if command -v cc >/dev/null 2>&1; then cc -O2 -std=c11 c/tree_structure_audit.c -o outputs/tree_structure_audit_c && ./outputs/tree_structure_audit_c > outputs/tables/c_tree_structure_audit.csv; else echo "cc not found; skipping."; fi

cpp:
	@$(MAKE) -C cpp run

fortran:
	@if command -v gfortran >/dev/null 2>&1; then gfortran -O2 fortran/tree_structure_quality_model.f90 -o outputs/tree_structure_quality_model_fortran && ./outputs/tree_structure_quality_model_fortran > outputs/tables/fortran_tree_structure_quality_model.txt; else echo "gfortran not found; skipping."; fi

java:
	@if command -v javac >/dev/null 2>&1 && command -v java >/dev/null 2>&1; then mkdir -p outputs/java_classes outputs/tables && javac -d outputs/java_classes java/src/main/java/org/contentcatalyst/algorithms/TreeStructureAudit.java && java -cp outputs/java_classes org.contentcatalyst.algorithms.TreeStructureAudit > outputs/tables/java_tree_structure_audit.csv; else echo "Java toolchain not found; skipping."; fi

typescript:
	@if command -v tsc >/dev/null 2>&1; then cd typescript && tsc --noEmit || true; else echo "tsc not found; skipping TypeScript without network install."; fi

prolog:
	@if command -v swipl >/dev/null 2>&1; then swipl -q -s prolog/tree_structure_rules.pl -g "ancestor(root, X), writeln(X), fail; halt." > outputs/tables/prolog_tree_structure_rules.txt; else echo "swipl not found; skipping."; fi

racket:
	@if command -v racket >/dev/null 2>&1; then racket racket/tree_structure_interpreter.rkt > outputs/tables/racket_tree_structure_interpreter.csv; else echo "racket not found; skipping."; fi

clean:
	rm -rf outputs/tables/* outputs/figures/* outputs/json/* outputs/logs/* outputs/reports/* outputs/java_classes outputs/tree_structure_audit_c outputs/tree_structure_quality_model_fortran
	$(MAKE) -C haskell clean || true
	$(MAKE) -C cpp clean || true
	cd rust && cargo clean || true
