#lang racket

(define (log2 x) (/ (log x) (log 2)))
(define (entropy probs)
  (- (for/sum ([p probs] #:when (> p 0))
       (* p (log2 p)))))

(displayln (format "entropy_bits=~a" (entropy '(0.5 0.5))))
