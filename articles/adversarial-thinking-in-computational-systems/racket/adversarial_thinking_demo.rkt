#lang racket

(define (readiness threat surface monitoring defense incident governance)
  (* 100 (+ (* 0.18 threat) (* 0.18 surface) (* 0.18 monitoring) (* 0.18 defense) (* 0.14 incident) (* 0.14 governance))))

(printf "adversarial readiness=~a\n" (readiness 0.86 0.82 0.88 0.82 0.80 0.78))
