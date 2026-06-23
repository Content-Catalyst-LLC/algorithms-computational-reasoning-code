#lang racket

(define hazard 0.80)
(define exposure 0.75)
(define vulnerability 0.60)
(define risk (* hazard exposure vulnerability))
(displayln (format "infrastructure_risk=~a" risk))
