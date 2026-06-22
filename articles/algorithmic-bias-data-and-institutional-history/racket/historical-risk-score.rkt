#lang racket

(define provenance-risk 0.66)
(define measurement-weakness 0.58)
(define proxy-risk 0.62)
(define remediation 0.42)
(define score (/ (+ provenance-risk measurement-weakness proxy-risk (- 1 remediation)) 4.0))
(displayln (format "historical_risk_score=~a" score))
