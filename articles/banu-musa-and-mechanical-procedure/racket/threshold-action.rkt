#lang racket

(define level 7.5)
(define threshold 5.0)
(displayln (format "action_triggered=~a" (>= level threshold)))
