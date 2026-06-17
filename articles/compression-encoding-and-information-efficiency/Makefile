.PHONY: all smoke python test calculator r julia sql haskell rust go c cpp fortran java typescript prolog racket clean

all: python test calculator r julia sql haskell rust go c cpp fortran java typescript prolog racket
smoke: python calculator sql

python:
	@if command -v python3 >/dev/null 2>&1; then PYTHONPATH=python python3 python/compression_encoding/cli.py; else echo "python3 not found; skipping."; fi

test:
	@if command -v python3 >/dev/null 2>&1 && python3 -c "import pytest" >/dev/null 2>&1; then PYTHONPATH=python python3 -m pytest python/tests; else echo "pytest not found; skipping tests."; fi

calculator:
	@if command -v python3 >/dev/null 2>&1; then PYTHONPATH=python python3 python/calculators/compression_ratio_calculator.py --output-dir outputs/json && PYTHONPATH=python python3 python/calculators/representation_quality_calculator.py --output-dir outputs/json; else echo "python3 not found; skipping calculator."; fi

r:
	@if command -v Rscript >/dev/null 2>&1; then Rscript r/compression_encoding_summary.R; else echo "Rscript not found; skipping."; fi

julia:
	@if command -v julia >/dev/null 2>&1; then mkdir -p outputs/tables && julia julia/entropy_examples.jl > outputs/tables/julia_compression_encoding_cases.csv; else echo "julia not found; skipping."; fi

sql:
	@if command -v sqlite3 >/dev/null 2>&1; then mkdir -p outputs/tables && sqlite3 outputs/tables/compression_encoding_cases.sqlite < sql/schema.sql && sqlite3 outputs/tables/compression_encoding_cases.sqlite < sql/analysis_queries.sql > outputs/tables/sql_compression_encoding_report.txt; else echo "sqlite3 not found; skipping."; fi

haskell:
	@$(MAKE) -C haskell run

rust:
	@if command -v cargo >/dev/null 2>&1; then cd rust && cargo run --quiet > ../outputs/tables/rust_compression_encoding_cases.csv; else echo "cargo not found; skipping."; fi

go:
	@if command -v go >/dev/null 2>&1; then cd go && go run main.go > ../outputs/tables/go_compression_encoding_cases.csv; else echo "go not found; skipping."; fi

c:
	@if command -v cc >/dev/null 2>&1; then cc -O2 -std=c11 c/compression_encoding_audit.c -o outputs/compression_encoding_audit_c && ./outputs/compression_encoding_audit_c > outputs/tables/c_compression_encoding_audit.csv; else echo "cc not found; skipping."; fi

cpp:
	@$(MAKE) -C cpp run

fortran:
	@if command -v gfortran >/dev/null 2>&1; then gfortran -O2 fortran/representation_quality_model.f90 -o outputs/representation_quality_model_fortran && ./outputs/representation_quality_model_fortran > outputs/tables/fortran_representation_quality_model.txt; else echo "gfortran not found; skipping."; fi

java:
	@if command -v javac >/dev/null 2>&1 && command -v java >/dev/null 2>&1; then mkdir -p outputs/java_classes outputs/tables && javac -d outputs/java_classes java/src/main/java/org/contentcatalyst/algorithms/CompressionEncodingAudit.java && java -cp outputs/java_classes org.contentcatalyst.algorithms.CompressionEncodingAudit > outputs/tables/java_compression_encoding_audit.csv; else echo "Java toolchain not found; skipping."; fi

typescript:
	@if command -v tsc >/dev/null 2>&1; then cd typescript && tsc --noEmit || true; else echo "tsc not found; skipping TypeScript without network install."; fi

prolog:
	@if command -v swipl >/dev/null 2>&1; then swipl -q -s prolog/compression_encoding_rules.pl -g "representation_quality(X, Y), write(X), write(','), writeln(Y), fail; halt." > outputs/tables/prolog_compression_encoding_rules.txt; else echo "swipl not found; skipping."; fi

racket:
	@if command -v racket >/dev/null 2>&1; then racket racket/compression_encoding_interpreter.rkt > outputs/tables/racket_compression_encoding_interpreter.csv; else echo "racket not found; skipping."; fi

clean:
	rm -rf outputs/tables/* outputs/figures/* outputs/json/* outputs/logs/* outputs/reports/* outputs/java_classes outputs/compression_encoding_audit_c outputs/representation_quality_model_fortran
	$(MAKE) -C haskell clean || true
	$(MAKE) -C cpp clean || true
	cd rust && cargo clean || true
