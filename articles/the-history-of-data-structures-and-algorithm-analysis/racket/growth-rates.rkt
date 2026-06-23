#lang racket

(for ([n '(10 100 1000 10000)])
  (define log2n (/ (log n) (log 2)))
  (displayln (format "n=~a, log2=~a, nlogn=~a, n2=~a" n log2n (* n log2n) (* n n))))
