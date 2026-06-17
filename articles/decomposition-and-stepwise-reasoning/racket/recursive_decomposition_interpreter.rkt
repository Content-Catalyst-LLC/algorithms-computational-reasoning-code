#lang racket

(struct decomposition-case (name subproblem boundary sequencing dependencies recomposition) #:transparent)

(define cases
  (list
   (decomposition-case "Search system" 82 78 82 72 72)
   (decomposition-case "Public decision-support workflow" 74 66 68 60 58)
   (decomposition-case "Scientific simulation" 86 82 80 78 82)
   (decomposition-case "Knowledge architecture" 80 76 74 70 80)))

(define (decomposition-score c)
  (+ (* 0.22 (decomposition-case-subproblem c))
     (* 0.20 (decomposition-case-boundary c))
     (* 0.18 (decomposition-case-sequencing c))
     (* 0.20 (decomposition-case-dependencies c))
     (* 0.20 (decomposition-case-recomposition c))))

(displayln "case_name,decomposition_score,warning")
(for ([c cases])
  (printf "~a,~a,Synthetic educational diagnostic only.~n"
          (decomposition-case-name c)
          (real->decimal-string (decomposition-score c) 3)))
