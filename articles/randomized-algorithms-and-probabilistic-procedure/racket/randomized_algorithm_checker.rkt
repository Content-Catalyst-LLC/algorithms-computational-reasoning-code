#lang racket
(define (amplification p k) (expt p k))
(displayln "test_name,value")
(displayln (format "amplification_failure,~a" (amplification 0.1 5)))
(displayln "seed,20260617")
