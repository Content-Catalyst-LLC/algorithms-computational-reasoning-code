#lang racket
(define (nondecreasing? xs)
  (or (empty? xs) (empty? (rest xs)) (and (<= (first xs) (second xs)) (nondecreasing? (rest xs)))))
(displayln "test_name,status")
(displayln (format "sorted_valid,~a" (if (nondecreasing? '(1 2 2 3)) "pass" "fail")))
(displayln (format "sorted_invalid,~a" (if (nondecreasing? '(1 3 2)) "pass" "fail")))
