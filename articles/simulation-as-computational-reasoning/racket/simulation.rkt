#lang racket
(define (step x) (max 0 (+ x (* 0.08 x) (- (* 0.03 x)) (- (* 0.04 x)))))
(for/fold ([stock 100.0]) ([t (in-range 31)])
  (printf "time_step=~a,stock=~a\n" t stock)
  (step stock))
