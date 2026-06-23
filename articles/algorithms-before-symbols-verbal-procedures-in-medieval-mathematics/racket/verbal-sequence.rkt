#lang racket

(define steps '("take the number" "double it" "add the adjustment" "check the result"))
(for ([step steps] [i (in-naturals 1)])
  (displayln (format "~a: ~a" i step)))
