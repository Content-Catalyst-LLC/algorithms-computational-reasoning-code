#lang racket
(define (precision-at-k tp k) (if (= k 0) 0 (/ tp k)))
(define (ranking-score l m f a s p) (* 100 (+ (* .22 l) (* .18 m) (* .12 f) (* .16 a) (* .17 s) (* .15 p))))
(displayln "test_name,value")
(displayln (format "precision_at_3,~a" (precision-at-k 2 3)))
(displayln (format "ranking_signal_score,~a" (ranking-score .84 .88 .76 .82 .78 .86)))
