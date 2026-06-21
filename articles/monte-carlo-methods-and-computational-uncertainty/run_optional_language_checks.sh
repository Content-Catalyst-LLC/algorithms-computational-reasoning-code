#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"
mkdir -p outputs/optional_checks

run_or_skip() {
  local name="$1"; shift
  if command -v "$1" >/dev/null 2>&1; then
    echo "==> Running $name"
    "$@" > "outputs/optional_checks/${name}.txt" 2>&1 || echo "$name failed; see outputs/optional_checks/${name}.txt"
  else
    echo "$name skipped: $1 not found" > "outputs/optional_checks/${name}_skipped.txt"
  fi
}

run_or_skip python_main python3 python/monte_carlo_methods_computational_uncertainty_audit.py
run_or_skip r_summary Rscript r/monte_carlo_methods_computational_uncertainty_summary.R
run_or_skip julia_demo julia julia/monte_carlo_demo.jl
run_or_skip rust_note rustc rust/monte_carlo_note.rs -o outputs/optional_checks/monte_carlo_note_rust
[ -x outputs/optional_checks/monte_carlo_note_rust ] && outputs/optional_checks/monte_carlo_note_rust >> outputs/optional_checks/rust_note.txt || true
run_or_skip go_note go run go/monte_carlo_note.go
run_or_skip c_note cc c/monte_carlo_note.c -o outputs/optional_checks/monte_carlo_note_c
[ -x outputs/optional_checks/monte_carlo_note_c ] && outputs/optional_checks/monte_carlo_note_c >> outputs/optional_checks/c_note.txt || true
run_or_skip cpp_note c++ cpp/monte_carlo_note.cpp -o outputs/optional_checks/monte_carlo_note_cpp
[ -x outputs/optional_checks/monte_carlo_note_cpp ] && outputs/optional_checks/monte_carlo_note_cpp >> outputs/optional_checks/cpp_note.txt || true
run_or_skip fortran_note gfortran fortran/monte_carlo_note.f90 -o outputs/optional_checks/monte_carlo_note_fortran
[ -x outputs/optional_checks/monte_carlo_note_fortran ] && outputs/optional_checks/monte_carlo_note_fortran >> outputs/optional_checks/fortran_note.txt || true
if command -v javac >/dev/null 2>&1 && command -v java >/dev/null 2>&1; then
  javac -d outputs/optional_checks java/MonteCarloNote.java > outputs/optional_checks/java_note.txt 2>&1 || true
  java -cp outputs/optional_checks MonteCarloNote >> outputs/optional_checks/java_note.txt 2>&1 || true
else
  echo "java_note skipped: javac/java not found" > outputs/optional_checks/java_note_skipped.txt
fi
run_or_skip typescript_note npx ts-node typescript/monte_carlo_note.ts
run_or_skip prolog_review swipl -q -s prolog/monte_carlo_review.pl -g responsible_monte_carlo_workflow -t halt
run_or_skip racket_note racket racket/monte_carlo_note.rkt
if command -v sqlite3 >/dev/null 2>&1; then
  sqlite3 outputs/optional_checks/monte_carlo_schema.sqlite < sql/monte_carlo_schema.sql
else
  echo "sqlite skipped: sqlite3 not found" > outputs/optional_checks/sqlite_skipped.txt
fi

echo "Optional checks complete."
