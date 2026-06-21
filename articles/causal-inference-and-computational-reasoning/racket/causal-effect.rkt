#lang racket

(define (effect treated-mean control-mean)
  (- treated-mean control-mean))

(displayln (format "causal contrast = ~a" (effect 0.64 0.47)))
