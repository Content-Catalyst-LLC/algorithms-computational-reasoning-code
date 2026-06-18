#lang racket
(define (missingness-rate missing total) (if (= total 0) 0 (/ missing total)))
(define (quality c v t p val) (* 100 (+ (* .25 c) (* .20 v) (* .15 t) (* .22 p) (* .18 val))))
(define mr (missingness-rate 45 1000))
(displayln "test_name,value")
(displayln (format "missingness_rate_45_of_1000,~a" mr))
(displayln (format "completeness_score_45_of_1000,~a" (- 1 mr)))
(displayln (format "data_quality_score,~a" (quality .92 .88 .86 .90 .89)))
