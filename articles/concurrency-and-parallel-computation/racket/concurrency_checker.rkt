#lang racket
(define (speedup t1 tp) (if (= tp 0) 0 (/ t1 tp)))
(define (amdahl p s) (if (= p 0) 0 (/ 1 (+ s (/ (- 1 s) p)))))
(define (efficiency p sp) (if (= p 0) 0 (/ sp p)))
(define sp (speedup 120 28))
(displayln "test_name,value")
(displayln (format "observed_speedup_120_to_28,~a" sp))
(displayln (format "amdahl_speedup_8_workers,~a" (amdahl 8 .12)))
(displayln (format "efficiency_8_workers,~a" (efficiency 8 sp)))
