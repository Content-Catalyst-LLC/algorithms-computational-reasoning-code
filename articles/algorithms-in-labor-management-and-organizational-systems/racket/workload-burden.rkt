#lang racket

(define pace 0.84)
(define hours 0.72)
(define fatigue 0.70)
(define schedule-volatility 0.78)
(define burden (/ (+ pace hours fatigue schedule-volatility) 4.0))
(displayln (format "workload_burden_score=~a" burden))
