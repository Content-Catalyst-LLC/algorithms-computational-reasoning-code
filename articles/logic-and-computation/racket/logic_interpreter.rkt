#lang racket

(struct logic-case (name rule predicate trace test governance) #:transparent)

(define cases
  (list
   (logic-case "Input validation rules" 82 84 68 82 70)
   (logic-case "Database query constraints" 78 80 72 76 72)
   (logic-case "Decision-rule workflow" 74 70 68 72 78)
   (logic-case "Program invariant checks" 80 78 74 80 66)))

(define (logic-quality c)
  (+ (* 0.24 (logic-case-rule c))
     (* 0.24 (logic-case-predicate c))
     (* 0.20 (logic-case-trace c))
     (* 0.18 (logic-case-test c))
     (* 0.14 (logic-case-governance c))))

(displayln "case_name,logic_quality,warning")
(for ([c cases])
  (printf "~a,~a,Synthetic educational diagnostic only.~n"
          (logic-case-name c)
          (real->decimal-string (logic-quality c) 3)))
