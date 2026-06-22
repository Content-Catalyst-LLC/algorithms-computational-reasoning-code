#lang racket

(define scores '(0.72 0.68 0.64 0.58 0.52 0.66))
(define capacity (/ (apply + scores) (length scores)))
(displayln (format "accountability_capacity_score=~a" capacity))
