#lang racket

(define scores '(0.62 0.58 0.46 0.52 0.60 0.58))
(define readiness (/ (apply + scores) (length scores)))
(displayln (format "delegation_readiness_score=~a" readiness))
