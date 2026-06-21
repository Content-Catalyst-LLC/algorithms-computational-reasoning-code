#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"
mkdir -p outputs/logs
run_optional() { local label="$1"; shift; echo "---- $label ----"; "$@" >"outputs/logs/${label}.log" 2>&1 || echo "$label failed or runtime missing; see outputs/logs/${label}.log"; }
command -v python3 >/dev/null 2>&1 && run_optional python python3 python/bayesian_computation_updating_beliefs_audit.py || echo "python3 not found"
command -v Rscript >/dev/null 2>&1 && run_optional r Rscript r/bayesian_computation_updating_beliefs_summary.R || echo "Rscript not found"
run_optional calculators bash calculators/run_calculator_smoke_tests.sh
command -v sqlite3 >/dev/null 2>&1 && run_optional sqlite sqlite3 :memory: ".read sql/example_bayesian_update.sql" || echo "sqlite3 not found"
command -v julia >/dev/null 2>&1 && run_optional julia julia julia/bayesian_update.jl || echo "julia not found"
command -v runghc >/dev/null 2>&1 && run_optional haskell runghc haskell/BayesianUpdate.hs || echo "runghc not found"
command -v cargo >/dev/null 2>&1 && run_optional rust cargo run --manifest-path rust/Cargo.toml || echo "cargo not found"
command -v go >/dev/null 2>&1 && run_optional go go run go/main.go || echo "go not found"
command -v gcc >/dev/null 2>&1 && run_optional c bash -lc "gcc c/bayesian_update.c -o outputs/logs/bayesian_update_c && outputs/logs/bayesian_update_c" || echo "gcc not found"
command -v g++ >/dev/null 2>&1 && run_optional cpp bash -lc "g++ cpp/bayesian_update.cpp -o outputs/logs/bayesian_update_cpp && outputs/logs/bayesian_update_cpp" || echo "g++ not found"
command -v gfortran >/dev/null 2>&1 && run_optional fortran bash -lc "gfortran fortran/bayesian_update.f90 -o outputs/logs/bayesian_update_fortran && outputs/logs/bayesian_update_fortran" || echo "gfortran not found"
command -v javac >/dev/null 2>&1 && command -v java >/dev/null 2>&1 && run_optional java bash -lc "javac java/BayesianUpdate.java -d outputs/logs && java -cp outputs/logs BayesianUpdate" || echo "javac/java not found"
command -v ts-node >/dev/null 2>&1 && run_optional typescript ts-node typescript/bayesian_update.ts || echo "ts-node not found"
command -v swipl >/dev/null 2>&1 && run_optional prolog swipl -q -f prolog/bayesian_update.pl || echo "swipl not found"
command -v racket >/dev/null 2>&1 && run_optional racket racket racket/bayesian_update.rkt || echo "racket not found"
