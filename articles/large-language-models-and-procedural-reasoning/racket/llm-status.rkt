#lang racket
(define (classify score stakes)
  (cond [(and (equal? stakes "high") (< score 1.0)) "escalate"]
        [(>= score 0.8) "pass"]
        [else "review"]))
(displayln (classify 0.67 "medium"))
