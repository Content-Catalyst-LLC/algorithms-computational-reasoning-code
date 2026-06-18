#lang racket
(define threshold (+ (* 5 10.0) 50.0))
(define offline 50.0)
(displayln "test_name,value")
(displayln (format "threshold_strategy,~a" threshold))
(displayln (format "offline_optimum,~a" offline))
(displayln (format "ratio,~a" (/ threshold offline)))
