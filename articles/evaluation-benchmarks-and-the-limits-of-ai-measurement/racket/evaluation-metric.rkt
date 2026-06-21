#lang racket

(define tp 42)
(define tn 38)
(define fp 7)
(define fn 13)
(define accuracy (/ (+ tp tn) (+ tp tn fp fn)))
(displayln (format "accuracy=~a" accuracy))
