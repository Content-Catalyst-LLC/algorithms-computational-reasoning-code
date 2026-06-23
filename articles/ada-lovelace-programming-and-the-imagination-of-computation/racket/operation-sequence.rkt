#lang racket

(define operations '("initialize" "store" "multiply" "subtract" "repeat" "output"))
(displayln (format "operation_count=~a" (length operations)))
(displayln (string-append "sequence=" (string-join operations " -> ")))
