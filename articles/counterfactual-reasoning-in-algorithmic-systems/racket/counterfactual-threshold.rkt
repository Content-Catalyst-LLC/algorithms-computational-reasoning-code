#lang racket

(define (label score threshold)
  (if (>= score threshold) 'favorable 'not-favorable))

(define original (label 0.57 0.62))
(define counterfactual (label 0.65 0.62))
(displayln (list 'original original))
(displayln (list 'counterfactual counterfactual))
(displayln (list 'decision-flipped (not (equal? original counterfactual))))
