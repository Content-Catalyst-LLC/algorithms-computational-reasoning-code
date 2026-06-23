#lang racket

(define (church-apply n f x)
  (if (= n 0)
      x
      (church-apply (- n 1) f (f x))))

(displayln (format "church_3_successor_0=~a" (church-apply 3 add1 0)))
