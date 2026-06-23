#lang racket

(define b 10.0)
(define c 39.0)
(define completion (sqr (/ b 2.0)))
(displayln (format "completion_term=~a" completion))
(displayln (format "completed_rhs=~a" (+ c completion)))
