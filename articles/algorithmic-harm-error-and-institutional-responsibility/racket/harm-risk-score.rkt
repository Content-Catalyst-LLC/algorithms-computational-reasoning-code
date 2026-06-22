#lang racket

(define error-likelihood 0.34)
(define severity 0.92)
(define exposure 0.78)
(define contestability 0.42)
(define harm-risk (* error-likelihood severity exposure (- 1 contestability)))
(displayln (format "harm_risk_score=~a" harm-risk))
