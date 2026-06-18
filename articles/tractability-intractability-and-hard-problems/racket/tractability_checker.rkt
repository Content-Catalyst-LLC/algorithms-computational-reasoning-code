#lang racket
(define (subset-count n) (expt 2 n))
(displayln "test_name,value")
(displayln (format "subsets_20,~a" (subset-count 20)))
(displayln "pairs_100,4950")
