#lang racket
(define observed '(33.1 39.7 38.8 39.3 8.4))
(define predicted '(31.92 31.58 36.48 25.30 11.30))
(define errors (map - observed predicted))
(define rmse (sqrt (/ (apply + (map (lambda (x) (* x x)) errors)) (length errors))))
(define mae (/ (apply + (map abs errors)) (length errors)))
(printf "rmse=~a\n" rmse)
(printf "mae=~a\n" mae)
