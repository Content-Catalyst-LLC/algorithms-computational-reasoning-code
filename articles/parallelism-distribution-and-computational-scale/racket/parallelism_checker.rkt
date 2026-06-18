#lang racket
(define (speedup s p) (/ 1 (+ s (/ (- 1 s) p))))
(define sp (speedup 0.10 16))
(displayln "test_name,value")
(displayln (format "speedup_p16_s010,~a" sp))
(displayln (format "efficiency_p16_s010,~a" (/ sp 16)))
