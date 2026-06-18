#lang racket
(define (freshness days decay) (exp (* -1 decay days)))
(define (quality v f c l m) (* 100 (+ (* .25 v) (* .18 f) (* .20 c) (* .22 l) (* .15 m))))
(displayln "test_name,value")
(displayln (format "freshness_3_days,~a" (freshness 3 .025)))
(displayln (format "pipeline_quality_score,~a" (quality .92 .86 .90 .88 .82)))
