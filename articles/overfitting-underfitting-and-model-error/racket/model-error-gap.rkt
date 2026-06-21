#lang racket
(define (generalization-gap train test) (- test train))
(displayln (generalization-gap 0.04 0.09))
