#lang racket
(define post-alpha (+ 2.0 113.0))
(define post-beta (+ 2.0 72.0))
(printf "posterior_mean=~a\n" (/ post-alpha (+ post-alpha post-beta)))
