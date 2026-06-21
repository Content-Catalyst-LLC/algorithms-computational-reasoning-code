#lang racket
(define (clamp v lo hi) (max lo (min hi v)))
(define (risk-model demand capacity failure-rate adaptation-rate noise)
  (clamp (+ 0.42 (* 0.38 demand) (* -0.31 capacity) (* 0.27 failure-rate) (* -0.18 adaptation-rate) noise) 0.0 1.0))
(displayln (risk-model 0.55 0.50 0.22 0.30 0.0))
