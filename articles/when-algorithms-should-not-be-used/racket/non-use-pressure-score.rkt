#lang racket

(define scores '(0.94 0.78 0.56 0.70))
(define pressure (/ (apply + scores) (length scores)))
(displayln (format "non_use_pressure_score=~a" pressure))
