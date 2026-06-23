#lang racket

(define value 12.0)
(define trigger 10.0)
(displayln (format "event_triggered=~a" (>= value trigger)))
