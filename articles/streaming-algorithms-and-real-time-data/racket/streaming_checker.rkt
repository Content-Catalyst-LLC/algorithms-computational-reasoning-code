#lang racket
(define arrival 90.0)
(define processing 100.0)
(displayln "test_name,value")
(displayln (format "utilization,~a" (/ arrival processing)))
(displayln (format "stable,~a" (< arrival processing)))
