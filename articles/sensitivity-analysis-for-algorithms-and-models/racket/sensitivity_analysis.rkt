#lang racket
(define (clamp x) (max 0 (min 1 x)))
(define (model demand capacity failure adaptation)
  (clamp (+ 0.5 (* 0.30 demand) (* 0.25 failure) (- (* 0.20 capacity)) (- (* 0.15 adaptation)))))
(displayln (format "baseline_risk=~a" (model 0.45 0.35 0.25 0.30)))
