#lang racket

(define (clamp x lo hi) (max lo (min hi x)))
(define (expected-net-value p benefit loss cost)
  (- (* (clamp p 0 1) benefit) (* (clamp p 0 1) loss) cost))

(displayln (expected-net-value 0.42 150 80 25))
