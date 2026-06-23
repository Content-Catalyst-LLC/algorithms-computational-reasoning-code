#lang racket

(define (sum-to n)
  (let loop ([i 0] [acc 0])
    (if (> i n)
        acc
        (loop (+ i 1) (+ acc i)))))

(displayln (format "sum_to_5=~a" (sum-to 5)))
