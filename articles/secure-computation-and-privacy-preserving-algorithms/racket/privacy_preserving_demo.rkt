#lang racket

(define updates '((100 . 0.42) (240 . 0.55) (160 . 0.49)))
(define total (apply + (map car updates)))
(define weighted (apply + (map (lambda (u) (* (car u) (cdr u))) updates)))
(printf "federated average weight=~a\n" (/ weighted total))
