#lang racket

(define (decision score threshold)
  (if (>= score threshold) 'act 'monitor))

(define baseline 0.42)
(define intervention 0.57)
(printf "estimated_effect=~a
" (- intervention baseline))
(printf "baseline_decision=~a
" (decision 0.53 0.55))
(printf "new_threshold_decision=~a
" (decision 0.53 0.50))
