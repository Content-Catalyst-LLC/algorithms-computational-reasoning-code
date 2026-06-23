#lang racket

(define due-process 0.58)
(define transparency 0.52)
(define human-review 0.60)
(define appeal-readiness 0.54)
(define score (/ (+ due-process transparency human-review appeal-readiness) 4.0))
(displayln (format "procedural_readiness_score=~a" score))
