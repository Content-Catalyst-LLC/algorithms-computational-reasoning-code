#lang racket
(define (relative-gap alg bound) (/ (- alg bound) bound))
(displayln "test_name,value")
(displayln (format "relative_gap,~a" (relative-gap 12 10)))
(displayln "approximation_ratio,1.5")
