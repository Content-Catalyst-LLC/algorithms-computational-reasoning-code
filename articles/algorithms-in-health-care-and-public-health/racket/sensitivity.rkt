#lang racket

(define tp 86.0)
(define fn 14.0)
(define sensitivity (/ tp (+ tp fn)))
(displayln (format "sensitivity=~a" sensitivity))
