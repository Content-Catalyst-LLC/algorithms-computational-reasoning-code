#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p outputs/logs outputs/bin

run_or_skip() {
  local cmd="$1"
  local log="$2"
  if command -v "${cmd%% *}" >/dev/null 2>&1; then
    bash -lc "$cmd" > "outputs/logs/$log" 2>&1 || echo "optional runtime failed: $cmd" >> "outputs/logs/$log"
  else
    echo "skipped; runtime not found: ${cmd%% *}" > "outputs/logs/$log"
  fi
}

run_or_skip "python3 python/uncertainty_quantification_computational_workflows_audit.py" "python_runtime.log"
run_or_skip "Rscript r/uncertainty_quantification_computational_workflows_summary.R" "r_runtime.log"
run_or_skip "julia julia/uncertainty_quantification_demo.jl" "julia_runtime.log"
run_or_skip "rustc rust/uncertainty_quantification.rs -o outputs/bin/uq_rust && outputs/bin/uq_rust" "rust_runtime.log"
run_or_skip "go run go/uncertainty_quantification.go" "go_runtime.log"
run_or_skip "gcc c/uncertainty_quantification.c -o outputs/bin/uq_c && outputs/bin/uq_c" "c_runtime.log"
run_or_skip "g++ -std=c++17 cpp/uncertainty_quantification.cpp -o outputs/bin/uq_cpp && outputs/bin/uq_cpp" "cpp_runtime.log"
run_or_skip "gfortran fortran/uncertainty_quantification.f90 -o outputs/bin/uq_fortran && outputs/bin/uq_fortran" "fortran_runtime.log"
run_or_skip "javac java/UncertaintyQuantification.java -d outputs/bin && java -cp outputs/bin UncertaintyQuantification" "java_runtime.log"
run_or_skip "node typescript/uncertainty_quantification.ts" "typescript_runtime.log"
run_or_skip "swipl -q -t halt -s prolog/uncertainty_quantification.pl" "prolog_runtime.log"
run_or_skip "racket racket/uncertainty_quantification.rkt" "racket_runtime.log"
run_or_skip "sqlite3 outputs/uncertainty_quantification.sqlite < sql/uncertainty_quantification_schema.sql" "sqlite_runtime.log"

echo "Optional runtime checks complete. See outputs/logs/."
