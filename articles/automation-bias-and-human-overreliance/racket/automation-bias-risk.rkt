#lang racket

(define acceptance 0.93)
(define quality 0.71)
(define uncertainty 0.29)
(define review-deficit 0.65)
(define override-friction 0.72)
(define weak-contestability 0.0)
(define overreliance-gap (max 0 (- acceptance quality)))
(define score (/ (+ acceptance overreliance-gap uncertainty review-deficit override-friction weak-contestability) 6.0))
(displayln (format "automation_bias_risk_score=~a" score))
