#lang racket

(define proxy-gap 0.38)
(define pressure 0.88)
(define gaming 0.72)
(define guardrail-penalty 1.0)
(define score (/ (+ proxy-gap pressure gaming guardrail-penalty) 4.0))
(displayln (format "goodhart_risk_score=~a" score))
