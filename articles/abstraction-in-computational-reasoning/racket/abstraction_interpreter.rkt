#lang racket

(struct abstraction-case (name clarity scope detail interpretation governance) #:transparent)

(define cases
  (list
   (abstraction-case "Search ranking" 82 70 62 60 56)
   (abstraction-case "Transit model" 78 72 66 72 66)
   (abstraction-case "Database schema" 84 78 70 74 70)
   (abstraction-case "Decision-support score" 70 60 48 52 66)))

(define (abstraction-score c)
  (+ (* 0.22 (abstraction-case-clarity c))
     (* 0.20 (abstraction-case-scope c))
     (* 0.20 (abstraction-case-detail c))
     (* 0.23 (abstraction-case-interpretation c))
     (* 0.15 (abstraction-case-governance c))))

(displayln "case_name,abstraction_score,warning")
(for ([c cases])
  (printf "~a,~a,Synthetic educational diagnostic only.~n"
          (abstraction-case-name c)
          (real->decimal-string (abstraction-score c) 3)))
