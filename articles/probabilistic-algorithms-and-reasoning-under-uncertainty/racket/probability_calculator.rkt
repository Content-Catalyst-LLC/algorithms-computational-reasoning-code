#lang racket
(define (standard-error p-hat n)
  (sqrt (/ (* p-hat (- 1 p-hat)) n)))
(displayln (hash 'p-hat 0.57 'n 1000 'standard-error (standard-error 0.57 1000)))
