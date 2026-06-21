#lang racket
(define tp 80.0)
(define fp 25.0)
(define tn 140.0)
(define fn 35.0)
(define total (+ tp fp tn fn))
(printf "accuracy=~a\n" (real->decimal-string (/ (+ tp tn) total) 6))
(printf "precision=~a\n" (real->decimal-string (/ tp (+ tp fp)) 6))
(printf "recall=~a\n" (real->decimal-string (/ tp (+ tp fn)) 6))
