#lang racket

(define total 1200.0)
(define weights '(2.0 1.0 1.0))
(define weight-sum (apply + weights))
(for ([w weights] [i (in-naturals 1)])
  (displayln (format "share_~a=~a" i (/ (* total w) weight-sum))))
