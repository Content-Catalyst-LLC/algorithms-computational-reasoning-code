.PHONY: all smoke python test calculator calculators r julia sql haskell rust go c cpp fortran java typescript prolog racket clean
all: python test calculator r julia sql haskell rust go c cpp fortran java typescript prolog racket
smoke: python calculator sql
python:
	@if command -v python3 >/dev/null 2>&1; then PYTHONPATH=python python3 python/ranking_relevance/cli.py; else echo "python3 not found; skipping."; fi
test:
	@if command -v python3 >/dev/null 2>&1 && python3 -c "import pytest" >/dev/null 2>&1; then PYTHONPATH=python python3 -m pytest python/tests; else echo "pytest not found; skipping tests."; fi
calculator:
	@if command -v python3 >/dev/null 2>&1; then bash calculators/run_calculator_smoke_tests.sh; else echo "python3 not found; skipping calculator."; fi
calculators: calculator
r:
	@if command -v Rscript >/dev/null 2>&1; then Rscript r/ranking_signal_summary.R; else echo "Rscript not found; skipping."; fi
julia:
	@if command -v julia >/dev/null 2>&1; then mkdir -p outputs/tables && julia julia/ranking_score_examples.jl > outputs/tables/julia_ranking_score_examples.csv; else echo "julia not found; skipping."; fi
sql:
	@if command -v sqlite3 >/dev/null 2>&1; then mkdir -p outputs/tables && sqlite3 outputs/tables/ranking_signal_examples.sqlite < sql/schema.sql && sqlite3 outputs/tables/ranking_signal_examples.sqlite < sql/ranking_quality_queries.sql > outputs/tables/sql_ranking_quality_report.txt; else echo "sqlite3 not found; skipping."; fi
haskell:
	@$(MAKE) -C haskell run
rust:
	@if command -v cargo >/dev/null 2>&1; then cd rust && cargo run --quiet > ../outputs/tables/rust_ranking_checks.csv; else echo "cargo not found; skipping."; fi
go:
	@if command -v go >/dev/null 2>&1; then cd go && go run main.go > ../outputs/tables/go_ranking_checks.csv; else echo "go not found; skipping."; fi
c:
	@if command -v cc >/dev/null 2>&1; then cc -O2 -std=c11 c/ranking_metrics.c -o outputs/ranking_metrics_c && ./outputs/ranking_metrics_c > outputs/tables/c_ranking_metrics.csv; else echo "cc not found; skipping."; fi
cpp:
	@$(MAKE) -C cpp run
fortran:
	@if command -v gfortran >/dev/null 2>&1; then gfortran -O2 fortran/ranking_score_model.f90 -o outputs/ranking_score_model_fortran && ./outputs/ranking_score_model_fortran > outputs/tables/fortran_ranking_score_model.txt; else echo "gfortran not found; skipping."; fi
java:
	@if command -v javac >/dev/null 2>&1 && command -v java >/dev/null 2>&1; then mkdir -p outputs/java_classes outputs/tables && javac -d outputs/java_classes java/src/main/java/org/contentcatalyst/algorithms/RankingSignalAudit.java && java -cp outputs/java_classes org.contentcatalyst.algorithms.RankingSignalAudit > outputs/tables/java_ranking_signal_checks.csv; else echo "Java toolchain not found; skipping."; fi
typescript:
	@if command -v tsc >/dev/null 2>&1; then cd typescript && tsc --noEmit || true; else echo "tsc not found; skipping TypeScript without network install."; fi
prolog:
	@if command -v swipl >/dev/null 2>&1; then swipl -q -s prolog/ranking_signal_rules.pl -g "ranking_signal(semantic),write('ranking_signal,semantic'),nl,halt." > outputs/tables/prolog_ranking_signal_rules.txt; else echo "swipl not found; skipping."; fi
racket:
	@if command -v racket >/dev/null 2>&1; then racket racket/ranking_checker.rkt > outputs/tables/racket_ranking_checks.csv; else echo "racket not found; skipping."; fi
clean:
	rm -rf outputs/tables/* outputs/figures/* outputs/json/* outputs/logs/* outputs/reports/* outputs/java_classes outputs/ranking_metrics_c outputs/ranking_score_model_fortran
	$(MAKE) -C haskell clean || true
	$(MAKE) -C cpp clean || true
	cd rust && cargo clean || true
