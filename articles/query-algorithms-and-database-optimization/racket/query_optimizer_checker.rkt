#lang racket
(define (selection-rows rows selectivity) (* rows selectivity))
(define (join-rows l r ld rd) (/ (* l r) (max ld rd)))
(displayln "test_name,value")
(displayln (format "selection_estimated_rows,~a" (selection-rows 1000000 .012)))
(displayln (format "join_estimated_rows,~a" (join-rows 500000 200000 50000 40000)))
