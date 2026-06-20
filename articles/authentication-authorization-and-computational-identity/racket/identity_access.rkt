#lang racket
(define weights '(0.10 0.11 0.11 0.09 0.09 0.10 0.09 0.09 0.08 0.06 0.06 0.02))
(define score (* 100 (apply + (map (lambda (w) (* 0.75 w)) weights))))
(displayln score)
