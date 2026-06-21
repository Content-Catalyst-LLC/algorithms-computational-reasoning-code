#lang racket
(define (f x) (+ (sin x) (* 0.25 x x)))
(define (central-difference x h) (/ (- (f (+ x h)) (f (- x h))) (* 2 h)))
(displayln (central-difference 1.0 0.01))
