#lang racket
(define (ranking-score text-match quality freshness diversity-bonus risk-penalty)
  (- (+ (* 0.36 text-match) (* 0.30 quality) (* 0.16 freshness) (* 0.14 diversity-bonus)) (* 0.20 risk-penalty)))
(displayln (real->decimal-string (ranking-score 0.92 0.88 0.60 0.35 0.04) 6))
