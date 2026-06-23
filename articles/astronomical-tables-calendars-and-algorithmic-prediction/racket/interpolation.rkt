#lang racket

(define x0 10.0)
(define y0 1.2)
(define x1 20.0)
(define y1 2.8)
(define x 15.0)
(define y (+ y0 (* (/ (- x x0) (- x1 x0)) (- y1 y0))))
(displayln (format "interpolated_y=~a" y))
