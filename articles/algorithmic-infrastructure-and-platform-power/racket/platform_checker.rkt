#lang racket
(define (dependency-score a v c s e) (* 100 (+ (* .22 a) (* .22 v) (* .18 c) (* .24 s) (* .14 e))))
(define (switching-cost m r t d l) (+ m r t d l))
(define (ratio n d) (if (= d 0) 0 (/ n d)))
(displayln "test_name,value")
(displayln (format "dependency_score,~a" (dependency-score .80 .90 .70 .85 .65)))
(displayln (format "switching_cost,~a" (switching-cost 45000 120000 18000 24000 75000)))
(displayln (format "api_dependency_ratio,~a" (ratio 850000 1000000)))
(displayln (format "visibility_share,~a" (ratio 250000 5000000)))
