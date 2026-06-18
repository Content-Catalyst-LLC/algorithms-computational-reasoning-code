#lang racket
(define (nlogn n) (* n (/ (log n) (log 2))))
(displayln "test_name,value")
(displayln "linear_1000,1000")
(displayln (format "nlogn_1000,~a" (nlogn 1000)))
(displayln "quadratic_1000,1000000")
