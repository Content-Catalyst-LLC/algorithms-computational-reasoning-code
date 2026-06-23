#lang racket

(define (formula x a b c)
  (+ (* a x x) (* b x) c))

(for ([x '(-2 -1 0 1 2 3)])
  (displayln (format "x=~a, y=~a" x (formula x 2 -3 1))))
