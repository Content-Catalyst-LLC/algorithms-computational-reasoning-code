#lang racket

(define notice 0.70)
(define reasons 0.62)
(define evidence-access 0.48)
(define human-review 0.55)
(define correction 0.52)
(define remedy 0.44)
(define score (/ (+ notice reasons evidence-access human-review correction remedy) 6.0))
(displayln (format "contestability_score=~a" score))
