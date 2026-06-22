#lang racket

(define amplification 0.82)
(define concentration 0.76)
(define intervention 0.44)
(define drift 0.28)
(define recursive-data 0.31)
(define score (/ (+ amplification concentration intervention drift recursive-data) 5.0))
(displayln (format "feedback_risk_score=~a" score))
