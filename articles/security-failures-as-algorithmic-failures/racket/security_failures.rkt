#lang racket
(define weights '(0.08 0.10 0.10 0.10 0.08 0.08 0.08 0.08 0.08 0.08 0.06 0.05 0.03))
(define score (* 100 (apply + (map (lambda (w) (* 0.65 w)) weights))))
(displayln score)
