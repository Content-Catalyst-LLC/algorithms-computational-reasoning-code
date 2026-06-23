#lang racket

(define (automation-risk stakes opacity delegation irreversibility)
  (max 0.0 (min 1.0 (* stakes opacity delegation irreversibility))))

(displayln (real->decimal-string (automation-risk 0.95 0.85 0.90 0.80) 6))
