#lang racket

(define input-drift 0.31)
(define label-drift 0.16)
(define performance-decay 0.10)
(define calibration-gap 0.14)
(define subgroup-gap 0.15)
(define override-rate 0.11)
(define score (/ (+ input-drift label-drift performance-decay calibration-gap subgroup-gap override-rate) 6.0))
(displayln (format "decay_risk_score=~a" score))
