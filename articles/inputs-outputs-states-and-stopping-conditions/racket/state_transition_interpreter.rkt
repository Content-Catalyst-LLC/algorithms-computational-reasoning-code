#lang racket

(struct boundary-case (name input output state stopping failure) #:transparent)

(define cases
  (list
   (boundary-case "Graph traversal" 84 80 86 80 70)
   (boundary-case "Decision-support workflow" 68 70 74 62 60)
   (boundary-case "Numerical simulation" 82 78 84 78 66)
   (boundary-case "Recommendation ranking" 74 72 70 60 52)))

(define (boundary-score c)
  (+ (* 0.22 (boundary-case-input c))
     (* 0.22 (boundary-case-output c))
     (* 0.22 (boundary-case-state c))
     (* 0.20 (boundary-case-stopping c))
     (* 0.14 (boundary-case-failure c))))

(displayln "case_name,boundary_score,warning")
(for ([c cases])
  (printf "~a,~a,Synthetic educational diagnostic only.~n"
          (boundary-case-name c)
          (real->decimal-string (boundary-score c) 3)))
