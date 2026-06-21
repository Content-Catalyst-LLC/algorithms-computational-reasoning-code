#!/usr/bin/env bash
set -Eeuo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

run_optional() {
  local label="$1"
  shift
  printf '\n[optional] %s\n' "$label"
  if "$@"; then
    printf '[ok] %s\n' "$label"
  else
    printf '[skip/fail nonblocking] %s\n' "$label"
  fi
}

if command -v python3 >/dev/null 2>&1; then
  python3 python/sensitivity_analysis_audit.py
else
  echo "python3 not found; skipping Python workflow"
fi

if command -v Rscript >/dev/null 2>&1; then
  Rscript r/sensitivity_summary.R
else
  echo "Rscript not found; skipping R workflow"
fi

bash calculators/run_calculator_smoke_tests.sh

run_optional "SQL parse with sqlite3" bash -lc 'command -v sqlite3 >/dev/null 2>&1 && sqlite3 :memory: < sql/sensitivity_schema.sql'
run_optional "Rust cargo check" bash -lc 'command -v cargo >/dev/null 2>&1 && (cd rust && cargo check)'
run_optional "Go run" bash -lc 'command -v go >/dev/null 2>&1 && (cd go && go run .)'
run_optional "C compile/run" bash -lc 'command -v cc >/dev/null 2>&1 && cc c/sensitivity_analysis.c -o outputs/logs/sensitivity_c && outputs/logs/sensitivity_c'
run_optional "C++ compile/run" bash -lc 'command -v c++ >/dev/null 2>&1 && c++ -std=c++17 cpp/sensitivity_analysis.cpp -o outputs/logs/sensitivity_cpp && outputs/logs/sensitivity_cpp'
run_optional "Fortran compile/run" bash -lc 'command -v gfortran >/dev/null 2>&1 && gfortran fortran/sensitivity_analysis.f90 -o outputs/logs/sensitivity_fortran && outputs/logs/sensitivity_fortran'
run_optional "Java compile/run" bash -lc 'command -v javac >/dev/null 2>&1 && command -v java >/dev/null 2>&1 && javac -d outputs/logs java/SensitivityAnalysis.java && java -cp outputs/logs SensitivityAnalysis'
run_optional "TypeScript compile" bash -lc 'command -v tsc >/dev/null 2>&1 && tsc typescript/sensitivity_analysis.ts --outDir outputs/logs --target ES2020 --module commonjs'
run_optional "Julia run" bash -lc 'command -v julia >/dev/null 2>&1 && julia julia/sensitivity_analysis.jl'
run_optional "Prolog consult" bash -lc 'command -v swipl >/dev/null 2>&1 && swipl -q -t halt -s prolog/sensitivity_analysis.pl'
run_optional "Racket run" bash -lc 'command -v racket >/dev/null 2>&1 && racket racket/sensitivity_analysis.rkt'
run_optional "Haskell syntax/run" bash -lc 'command -v runghc >/dev/null 2>&1 && runghc haskell/SensitivityAnalysis.hs'
