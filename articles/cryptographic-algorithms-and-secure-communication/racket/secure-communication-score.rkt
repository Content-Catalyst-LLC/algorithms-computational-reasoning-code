#lang racket

(define (score threat-model keys validation integrity authentication)
  (* 100 (+ (* 0.22 threat-model) (* 0.24 keys) (* 0.18 validation) (* 0.18 integrity) (* 0.18 authentication))))

(displayln (format "standard secure channel score=~a" (real->decimal-string (score 0.86 0.82 0.90 0.86 0.84) 2)))
(displayln (format "legacy manual transfer score=~a" (real->decimal-string (score 0.36 0.24 0.18 0.34 0.28) 2)))
