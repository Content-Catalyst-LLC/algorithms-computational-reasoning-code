#lang racket
(define (schema-quality f k c m l) (* 100 (+ (* .22 f) (* .20 k) (* .20 c) (* .20 m) (* .18 l))))
(displayln "test_name,value")
(displayln (format "schema_quality_score,~a" (schema-quality .90 .85 .80 .88 .82)))
