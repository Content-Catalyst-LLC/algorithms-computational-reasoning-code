#lang racket
(define (rate num den) (if (= den 0) 0 (/ num den)))
(displayln (format "false-negative-rate=~a" (real->decimal-string (rate 22 94) 4)))
