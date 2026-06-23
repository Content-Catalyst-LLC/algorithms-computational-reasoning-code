#lang racket

(define scores '(0.96 0.98 0.96 0.88 0.98 0.90 0.90 0.96 0.98 0.98))
(define score (/ (apply + scores) (length scores)))
(displayln (format "origin_care_score=~a" score))
