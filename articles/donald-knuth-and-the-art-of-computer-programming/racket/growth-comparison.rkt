#lang racket

(define n 1000.0)
(define log2n (/ (log n) (log 2)))

(displayln (format "log2_n=~a" log2n))
(displayln (format "n=~a" n))
(displayln (format "n_log2_n=~a" (* n log2n)))
(displayln (format "n_squared=~a" (* n n)))
