#lang racket

(define facts '(has_documentation logs_decisions))
(define premises '(has_documentation logs_decisions))
(define rule-fires? (andmap (lambda (p) (member p facts)) premises))
(displayln (format "rule_fires=~a" (if rule-fires? "true" "false")))
