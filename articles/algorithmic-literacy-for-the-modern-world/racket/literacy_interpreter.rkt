#lang racket

(struct literacy-case (name transparency interpretability contestability governance judgment) #:transparent)

(define cases
  (list
   (literacy-case "Search ranking" 62 66 38 52 68)
   (literacy-case "Public decision-support workflow" 58 56 70 76 74)
   (literacy-case "Scientific simulation dashboard" 76 74 60 68 80)
   (literacy-case "Recommendation feed" 40 48 32 46 50)))

(define (literacy-score c)
  (+ (* 0.22 (literacy-case-transparency c))
     (* 0.22 (literacy-case-interpretability c))
     (* 0.18 (literacy-case-contestability c))
     (* 0.18 (literacy-case-governance c))
     (* 0.20 (literacy-case-judgment c))))

(displayln "case_name,literacy_support_score,warning")
(for ([c cases])
  (printf "~a,~a,Synthetic educational diagnostic only.~n"
          (literacy-case-name c)
          (real->decimal-string (literacy-score c) 3)))
