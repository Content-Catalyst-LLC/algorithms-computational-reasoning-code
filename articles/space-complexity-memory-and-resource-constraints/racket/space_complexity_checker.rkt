#lang racket
(define v 1000)
(define e 5000)
(displayln "test_name,value")
(displayln (format "matrix_units,~a" (* v v)))
(displayln (format "adjacency_list_units,~a" (+ v e)))
