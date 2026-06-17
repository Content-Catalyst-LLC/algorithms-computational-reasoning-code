#lang racket
(define (score-in-range? x) (and (>= x 0) (<= x 100)))
(displayln "test_name,status")
(displayln (format "score_72,~a" (if (score-in-range? 72) "pass" "fail")))
(displayln (format "score_150,~a" (if (score-in-range? 150) "pass" "fail")))
