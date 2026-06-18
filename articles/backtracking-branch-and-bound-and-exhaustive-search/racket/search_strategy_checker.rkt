#lang racket
(define (growth b d)
  (for/sum ([level (in-range 0 (+ d 1))]) (expt b level)))
(displayln "test_name,value")
(displayln (format "search_space_growth,~a" (growth 2 3)))
(displayln "permutation_count,6")
