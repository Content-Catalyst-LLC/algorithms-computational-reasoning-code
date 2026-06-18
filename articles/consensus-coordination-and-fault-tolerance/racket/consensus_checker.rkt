#lang racket
(define (mq n) (+ (quotient n 2) 1))
(define (ft n) (quotient (- n 1) 2))
(define (bft f) (+ (* 3 f) 1))
(displayln "test_name,value")
(displayln (format "majority_quorum_5_nodes,~a" (mq 5)))
(displayln (format "crash_fault_tolerance_5_nodes,~a" (ft 5)))
(displayln (format "byzantine_replicas_for_2_faults,~a" (bft 2)))
