#lang racket

(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))

(for ([i (in-range 0 7)])
  (displayln (list i (factorial i))))
