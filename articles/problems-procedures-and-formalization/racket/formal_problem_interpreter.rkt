#lang racket

(struct formal-case (name input output objective assumptions governance) #:transparent)

(define cases
  (list
   (formal-case "Document search" 82 78 70 58 56)
   (formal-case "Worker scheduling" 72 76 58 54 62)
   (formal-case "Public service triage" 60 72 52 46 66)
   (formal-case "Scientific simulation" 86 80 76 84 70)))

(define (formalization-score c)
  (+ (* 0.20 (formal-case-input c))
     (* 0.20 (formal-case-output c))
     (* 0.25 (formal-case-objective c))
     (* 0.20 (formal-case-assumptions c))
     (* 0.15 (formal-case-governance c))))

(displayln "case_name,formalization_score,warning")
(for ([c cases])
  (printf "~a,~a,Synthetic educational diagnostic only.~n"
          (formal-case-name c)
          (real->decimal-string (formalization-score c) 3)))
