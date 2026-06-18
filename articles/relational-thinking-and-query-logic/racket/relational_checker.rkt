#lang racket
(define (query-score e r p j k m) (* 100 (+ (* .18 e) (* .18 r) (* .18 p) (* .18 j) (* .14 k) (* .14 m))))
(displayln "test_name,value")
(displayln (format "query_logic_core_score,~a" (query-score .88 .86 .84 .82 .84 .80)))
