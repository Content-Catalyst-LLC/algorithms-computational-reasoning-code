#lang racket

(define scores '(0.60 0.62 0.58 0.52 0.46 0.50))
(define readiness (/ (apply + scores) (length scores)))
(displayln (format "governance_readiness_score=~a" readiness))
