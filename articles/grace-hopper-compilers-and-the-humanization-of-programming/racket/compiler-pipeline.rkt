#lang racket

(define source "ADD PAYROLL-TOTAL TO TAX-BASE")
(define tokens (string-split source))

(displayln (format "source=~a" source))
(displayln (format "tokens=~a" tokens))
(displayln "target_code=machine-specific instruction sequence")
