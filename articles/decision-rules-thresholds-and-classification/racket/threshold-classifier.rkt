#lang racket

(define (classify score threshold)
  (if (>= score threshold) 1 0))

(displayln (classify 0.72 0.50))
