#lang racket

(define scores '(0.98 0.90 0.94 0.88 0.94 0.90 0.96 0.84 0.96))
(define score (/ (apply + scores) (length scores)))
(displayln (format "transfer_score=~a" score))
