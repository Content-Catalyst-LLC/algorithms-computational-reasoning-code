#lang racket

(define scores '(0.62 0.6875 0.58 0.50 0.56 0.52))
(define quality (/ (apply + scores) (length scores)))
(displayln (format "documentation_quality_score=~a" quality))
