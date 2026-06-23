#lang racket
(define (delegation-risk a b c) (max 0.0 (min 1.0 (* a b c))))
(displayln (real->decimal-string (delegation-risk 0.95 0.95 0.80) 6))
