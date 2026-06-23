#lang racket

(define pd 0.035)
(define lgd 0.45)
(define ead 100000.0)
(define expected-loss (* pd lgd ead))
(displayln (format "expected_loss=~a" expected-loss))
