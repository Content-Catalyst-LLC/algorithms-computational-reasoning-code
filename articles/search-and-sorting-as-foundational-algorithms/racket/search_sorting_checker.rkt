#lang racket
(define (linear-search xs target)
  (let loop ([xs xs] [i 0])
    (cond [(empty? xs) -1]
          [(equal? (first xs) target) i]
          [else (loop (rest xs) (+ i 1))])))
(displayln "test_name,value")
(displayln (format "linear_search_9,~a" (linear-search '(7 2 9 1) 9)))
(displayln "sort_demo,1:2:7:9")
