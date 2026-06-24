#lang racket

(define (threshold-unit inputs weights threshold)
  (define total (apply + (map * inputs weights)))
  (if (>= total threshold) 1 0))

(displayln (threshold-unit '(1 1) '(1 1) 2))
