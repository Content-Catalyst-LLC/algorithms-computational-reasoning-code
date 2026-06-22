#lang racket

(define likelihood 0.42)
(define severity 0.86)
(define detectability 0.38)
(define controllability 0.44)
(define failure-risk (* likelihood severity (- 1 detectability) (- 1 controllability)))
(displayln (format "failure_risk_score=~a" failure-risk))
