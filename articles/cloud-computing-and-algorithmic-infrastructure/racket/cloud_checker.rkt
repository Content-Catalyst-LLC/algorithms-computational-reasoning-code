#lang racket
(define (total-latency c s n q o) (+ c s n q o))
(define (nominal-capacity nodes cap) (* nodes cap))
(define (unit-cost c s n m o completed) (if (= completed 0) 0 (/ (+ c s n m o) completed)))
(displayln "test_name,value")
(displayln (format "cloud_response_latency_ms,~a" (total-latency 80 45 60 25 15)))
(displayln (format "nominal_capacity,~a" (nominal-capacity 12 250)))
(displayln (format "unit_cost,~a" (unit-cost 120 35 25 90 18 144000)))
