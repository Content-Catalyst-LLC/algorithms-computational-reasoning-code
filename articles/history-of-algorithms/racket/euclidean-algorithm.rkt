#lang racket

(define (gcd-algorithm a b)
  (if (= b 0)
      (abs a)
      (gcd-algorithm b (remainder a b))))

(displayln (format "gcd=~a" (gcd-algorithm 252 105)))
