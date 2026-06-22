#lang racket

(define rates '(0.42 0.31 0.36))
(define selection-gap (- (apply max rates) (apply min rates)))
(displayln (format "selection_gap=~a" selection-gap))
