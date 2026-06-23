#lang racket

(define pretest 0.52)
(define posttest 0.78)
(define gain (- posttest pretest))
(displayln (format "learning_gain=~a" gain))
