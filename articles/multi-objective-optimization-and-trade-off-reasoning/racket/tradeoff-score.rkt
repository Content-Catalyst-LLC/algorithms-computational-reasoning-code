#lang racket
(define scores '((A . 0.52) (B . 0.49) (C . 0.82) (D . 0.35)))
(sort scores > #:key cdr)
