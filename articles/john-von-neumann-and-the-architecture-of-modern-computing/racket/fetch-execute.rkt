#lang racket

(define program '((LOAD 2) (ADD 3) (STORE 0) (HALT 0)))
(define acc 0)

(for ([inst program])
  (match inst
    [`(LOAD ,x) (set! acc x)]
    [`(ADD ,x) (set! acc (+ acc x))]
    [`(STORE ,addr) (displayln (format "store address=~a value=~a" addr acc))]
    [`(HALT ,_) (displayln (format "halt accumulator=~a" acc))]))
