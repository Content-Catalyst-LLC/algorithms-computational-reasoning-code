#lang racket
(define (expected-reward p value cost) (- (* p value) cost))
(displayln (expected-reward 0.54 1.0 0.08))
