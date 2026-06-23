#lang racket

(define engagement-pressure 0.92)
(define creator-impact 0.88)
(define public-knowledge-impact 0.78)
(define user-control 0.44)
(define contestability 0.42)
(define score (/ (+ engagement-pressure creator-impact public-knowledge-impact (- 1 user-control) (- 1 contestability)) 5.0))
(displayln (format "attention_risk_score=~a" score))
