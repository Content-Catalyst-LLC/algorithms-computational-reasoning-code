#lang racket

(define languages
  (hash "Fortran" "scientific numerical programming"
        "Lisp" "symbolic computation"
        "SQL" "declarative data querying"
        "Rust" "memory-safe systems programming"))

(for ([(language trait) (in-hash languages)])
  (displayln (format "~a: ~a" language trait)))
