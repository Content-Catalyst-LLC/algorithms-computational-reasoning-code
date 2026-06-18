#lang racket
(define (efficiency-gain baseline optimized) (/ (- baseline optimized) baseline))
(displayln "test_name,value")
(displayln (format "efficiency_gain_percent,~a" (* 100 (efficiency-gain 100.0 64.0))))
