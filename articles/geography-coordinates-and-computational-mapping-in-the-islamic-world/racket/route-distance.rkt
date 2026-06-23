#lang racket

(define segments '(12.0 20.0 7.5))
(displayln (format "segments=~a" (length segments)))
(displayln (format "total_distance=~a" (apply + segments)))
