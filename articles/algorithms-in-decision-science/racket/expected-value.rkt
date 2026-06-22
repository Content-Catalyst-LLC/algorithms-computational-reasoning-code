#lang racket

(define probability 0.82)
(define benefit-if-act 0.88)
(define cost-if-act 0.30)
(define expected-value (- (* probability benefit-if-act) cost-if-act))
(displayln (format "expected_value_of_action=~a" expected-value))
