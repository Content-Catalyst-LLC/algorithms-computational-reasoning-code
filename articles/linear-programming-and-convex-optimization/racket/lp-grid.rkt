#lang racket
(define (feasible? x y) (and (<= (+ (* 2 x) y) 8) (<= (+ x (* 2 y)) 8)))
(define (objective x y) (+ (* 3 x) (* 4 y)))
(define candidates
  (for*/list ([x (in-range 10)] [y (in-range 10)] #:when (feasible? x y))
    (list (objective x y) x y)))
(displayln (argmax first candidates))
