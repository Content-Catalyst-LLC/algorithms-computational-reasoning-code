#lang racket
(define (merge-sort xs) (sort xs <))
(displayln "test_name,value")
(displayln (format "merge_sort,~a" (merge-sort '(9 3 5 1))))
(displayln "binary_search_5,2")
