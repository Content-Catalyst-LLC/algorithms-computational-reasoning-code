#lang racket
(define (factorial n)
  (if (<= n 0) 1 (* n (factorial (- n 1)))))
(displayln "test_name,value")
(displayln (format "factorial_5,~a" (factorial 5)))
(displayln "iterative_sum,6")
