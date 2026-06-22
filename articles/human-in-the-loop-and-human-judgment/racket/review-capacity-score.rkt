#lang racket

(define scores '(0.56 0.62 0.58 0.60 0.48))
(define capacity (/ (apply + scores) (length scores)))
(displayln (format "review_capacity_score=~a" capacity))
