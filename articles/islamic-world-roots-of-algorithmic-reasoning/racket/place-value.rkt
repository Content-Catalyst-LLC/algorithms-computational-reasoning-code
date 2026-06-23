#lang racket

(define digit 7)
(define base 10)
(define position 3)
(define value (* digit (expt base position)))
(displayln (format "place_value=~a" value))
