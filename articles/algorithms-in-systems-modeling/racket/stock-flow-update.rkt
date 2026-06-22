#lang racket

(define current-stock 100.0)
(define inflow 12.0)
(define outflow 7.0)
(define next-stock (- (+ current-stock inflow) outflow))
(displayln (format "next_stock=~a" next-stock))
