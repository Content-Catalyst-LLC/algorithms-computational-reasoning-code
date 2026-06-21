#lang racket
(define (generalization-gap train test) (- train test))
(displayln (generalization-gap 0.88 0.81))
