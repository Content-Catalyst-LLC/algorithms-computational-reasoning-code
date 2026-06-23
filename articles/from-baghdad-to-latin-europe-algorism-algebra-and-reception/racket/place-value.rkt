#lang racket

(define digits '(1 2 3 0))
(define value (foldl (lambda (digit acc) (+ (* acc 10) digit)) 0 digits))
(displayln (format "place_value=~a" value))
