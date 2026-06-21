#!/usr/bin/env bash
set -u

ARTICLE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ARTICLE_DIR"
mkdir -p outputs/logs outputs/bin
LOG="outputs/logs/optional_language_checks.log"
: > "$LOG"

run_check() {
  local label="$1"
  shift
  printf '\n==> %s\n' "$label" | tee -a "$LOG"
  "$@" >> "$LOG" 2>&1
  local status=$?
  if [[ $status -eq 0 ]]; then
    printf 'PASS: %s\n' "$label" | tee -a "$LOG"
  else
    printf 'SKIP/FAIL: %s (status %s)\n' "$label" "$status" | tee -a "$LOG"
  fi
}

if command -v python3 >/dev/null 2>&1; then
  run_check "Python syntax" python3 -m py_compile python/computational_experiments_reproducible_workflows_audit.py calculators/python/workflow_calculator.py
fi

if command -v Rscript >/dev/null 2>&1; then
  run_check "R scripts parse" Rscript -e 'parse("r/computational_experiments_reproducible_workflows_summary.R"); parse("calculators/r/workflow_calculator.R"); cat("R parse OK\n")'
fi

if command -v sqlite3 >/dev/null 2>&1; then
  run_check "SQLite schema" bash -lc 'sqlite3 outputs/reproducible_workflows_schema.sqlite < sql/reproducible_workflows_schema.sql && sqlite3 outputs/reproducible_workflows_schema.sqlite ".tables"'
fi

if command -v go >/dev/null 2>&1; then
  run_check "Go scaffold" go run go/reproducible_workflow.go
fi

if command -v rustc >/dev/null 2>&1; then
  run_check "Rust scaffold" bash -lc 'rustc rust/reproducible_workflow.rs -o outputs/bin/reproducible_workflow_rust && outputs/bin/reproducible_workflow_rust'
fi

if command -v gcc >/dev/null 2>&1; then
  run_check "C scaffold" bash -lc 'gcc c/reproducible_workflow.c -o outputs/bin/reproducible_workflow_c && outputs/bin/reproducible_workflow_c'
fi

if command -v g++ >/dev/null 2>&1; then
  run_check "C++ scaffold" bash -lc 'g++ cpp/reproducible_workflow.cpp -o outputs/bin/reproducible_workflow_cpp && outputs/bin/reproducible_workflow_cpp'
fi

if command -v gfortran >/dev/null 2>&1; then
  run_check "Fortran scaffold" bash -lc 'gfortran fortran/reproducible_workflow.f90 -o outputs/bin/reproducible_workflow_fortran && outputs/bin/reproducible_workflow_fortran'
fi

if command -v javac >/dev/null 2>&1 && command -v java >/dev/null 2>&1; then
  run_check "Java scaffold" bash -lc 'javac -d outputs/bin java/ReproducibleWorkflow.java && java -cp outputs/bin ReproducibleWorkflow'
else
  printf '\n==> Java compiler/runtime not found; skipping Java scaffold.\n' | tee -a "$LOG"
fi

if command -v node >/dev/null 2>&1; then
  run_check "TypeScript syntax note" bash -lc 'printf "TypeScript scaffold present: typescript/reproducible_workflow.ts\n"'
fi

if command -v julia >/dev/null 2>&1; then
  run_check "Julia scaffold" julia julia/reproducible_workflow_summary.jl
fi

if command -v swipl >/dev/null 2>&1; then
  run_check "Prolog scaffold" swipl -q -s prolog/reproducible_workflow.pl -g review_complete -t halt
fi

if command -v racket >/dev/null 2>&1; then
  run_check "Racket scaffold" racket racket/reproducible_workflow.rkt
fi

if command -v ghc >/dev/null 2>&1; then
  run_check "Haskell scaffold" bash -lc 'ghc -outputdir outputs/bin -o outputs/bin/reproducible_workflow_hs haskell/ReproducibleWorkflow.hs && outputs/bin/reproducible_workflow_hs'
else
  printf '\n==> Haskell compiler not found; scaffold documented only.\n' | tee -a "$LOG"
fi

printf '\n==> Optional language checks complete. See %s\n' "$LOG"
