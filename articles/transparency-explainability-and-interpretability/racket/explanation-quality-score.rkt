#lang racket

(define scores '(0.70 0.74 0.62 0.58 0.46))
(define quality (/ (apply + scores) (length scores)))
(displayln (format "explanation_quality_score=~a" quality))
