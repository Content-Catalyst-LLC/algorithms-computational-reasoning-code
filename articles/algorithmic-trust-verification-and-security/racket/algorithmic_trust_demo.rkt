#lang racket

(define (trust-quality verification validation security provenance monitoring governance)
  (* 100 (+ (* 0.18 verification) (* 0.18 validation) (* 0.18 security) (* 0.16 provenance) (* 0.15 monitoring) (* 0.15 governance))))

(printf "trust quality=~a\n" (trust-quality 0.88 0.82 0.88 0.90 0.84 0.82))
