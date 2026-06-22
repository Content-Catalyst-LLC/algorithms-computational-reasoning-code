#lang racket

(define validity-gap 0.42)
(define missingness 0.12)
(define differential-error 0.24)
(define label-error 0.08)
(define score (/ (+ validity-gap missingness differential-error label-error) 4.0))
(displayln (format "measurement_risk_score=~a" score))
