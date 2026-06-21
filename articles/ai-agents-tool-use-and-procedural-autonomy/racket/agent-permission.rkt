#lang racket

(define risk 0.85)
(define approval-required #t)
(define approved #f)

(define status
  (cond
    [(and approval-required (not approved)) "blocked"]
    [(>= risk 0.65) "escalate"]
    [else "pass"]))

(displayln (format "agent_action_status=~a" status))
