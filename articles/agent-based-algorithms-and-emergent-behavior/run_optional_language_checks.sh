#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

echo "==> Optional language checks for Agent-Based Algorithms and Emergent Behavior"

if command -v python3 >/dev/null 2>&1; then
  python3 -m py_compile python/agent_based_algorithms_emergent_behavior_audit.py calculators/python/agent_based_calculator.py
else
  echo "python3 not found; skipping Python checks."
fi

if command -v Rscript >/dev/null 2>&1; then
  Rscript -e 'parse(file="r/agent_based_algorithms_emergent_behavior_summary.R"); parse(file="calculators/r/model_calculator.R"); cat("R parse checks passed\n")'
else
  echo "Rscript not found; skipping R checks."
fi

if command -v sqlite3 >/dev/null 2>&1; then
  sqlite3 /tmp/agent_based_schema_check.sqlite < sql/agent_based_schema.sql
  rm -f /tmp/agent_based_schema_check.sqlite
else
  echo "sqlite3 not found; skipping SQL schema check."
fi

if command -v node >/dev/null 2>&1; then
  node -e 'console.log("Node present; TypeScript scaffold is source-only unless tsc is installed.")'
else
  echo "node not found; skipping TypeScript runtime note."
fi

if command -v go >/dev/null 2>&1; then
  go run go/agent_based_notes.go
else
  echo "go not found; skipping Go check."
fi

if command -v rustc >/dev/null 2>&1; then
  rustc rust/agent_based_notes.rs -o /tmp/agent_based_notes_rs && /tmp/agent_based_notes_rs && rm -f /tmp/agent_based_notes_rs
else
  echo "rustc not found; skipping Rust check."
fi

if command -v gcc >/dev/null 2>&1; then
  gcc c/agent_based_notes.c -o /tmp/agent_based_notes_c && /tmp/agent_based_notes_c && rm -f /tmp/agent_based_notes_c
else
  echo "gcc not found; skipping C check."
fi

if command -v g++ >/dev/null 2>&1; then
  g++ cpp/agent_based_notes.cpp -o /tmp/agent_based_notes_cpp && /tmp/agent_based_notes_cpp && rm -f /tmp/agent_based_notes_cpp
else
  echo "g++ not found; skipping C++ check."
fi

if command -v gfortran >/dev/null 2>&1; then
  gfortran fortran/agent_based_notes.f90 -o /tmp/agent_based_notes_f90 && /tmp/agent_based_notes_f90 && rm -f /tmp/agent_based_notes_f90
else
  echo "gfortran not found; skipping Fortran check."
fi

if command -v javac >/dev/null 2>&1 && command -v java >/dev/null 2>&1; then
  javac java/AgentBasedNotes.java
  java -cp java AgentBasedNotes
  rm -f java/AgentBasedNotes.class
else
  echo "javac/java not found; skipping Java check."
fi

if command -v julia >/dev/null 2>&1; then
  julia julia/agent_based_summary.jl
else
  echo "julia not found; skipping Julia check."
fi

if command -v swipl >/dev/null 2>&1; then
  swipl -q -t halt -s prolog/agent_based_notes.pl
else
  echo "swipl not found; skipping Prolog check."
fi

if command -v racket >/dev/null 2>&1; then
  racket racket/agent_based_notes.rkt
else
  echo "racket not found; skipping Racket check."
fi

if command -v ghc >/dev/null 2>&1; then
  ghc -fno-code haskell/AgentBasedNotes.hs
else
  echo "ghc not found; skipping Haskell check."
fi
