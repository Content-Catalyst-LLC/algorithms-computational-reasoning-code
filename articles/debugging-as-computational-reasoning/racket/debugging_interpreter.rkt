#lang racket

(struct debug-case (name reproduce trace isolate verify regression) #:transparent)

(define cases
  (list
   (debug-case "Graph traversal infinite loop" 88 78 80 82 78)
   (debug-case "Data pipeline missing-value bug" 84 74 72 76 74)
   (debug-case "Simulation instability" 80 78 70 74 66)
   (debug-case "Recommendation ranking tie bug" 76 68 70 72 70)))

(define (debugging-quality c)
  (+ (* 0.22 (debug-case-reproduce c))
     (* 0.20 (debug-case-trace c))
     (* 0.18 (debug-case-isolate c))
     (* 0.22 (debug-case-verify c))
     (* 0.18 (debug-case-regression c))))

(displayln "case_name,debugging_quality,warning")
(for ([c cases])
  (printf "~a,~a,Synthetic educational diagnostic only.~n"
          (debug-case-name c)
          (real->decimal-string (debugging-quality c) 3)))
