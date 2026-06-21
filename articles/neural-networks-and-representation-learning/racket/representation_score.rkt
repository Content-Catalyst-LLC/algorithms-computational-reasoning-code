#lang racket
(define (sigmoid x) (/ 1 (+ 1 (exp (- x)))))
(define (representation-score x1 x2 x3 [bias 0.0])
  (sigmoid (+ (* 0.9 x1) (* -0.7 x2) (* 0.35 x3) bias)))
(displayln (real->decimal-string (representation-score 0.5 -0.2 0.7) 6))
