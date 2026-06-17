#lang racket

(struct translation-case (name intent control edge tests maintain) #:transparent)

(define cases
  (list
   (translation-case "Search ranking prototype" 82 80 64 68 72)
   (translation-case "Decision-rule implementation" 76 74 66 62 68)
   (translation-case "Simulation loop" 84 82 72 70 74)
   (translation-case "Data-cleaning procedure" 78 76 70 66 72)))

(define (translation-quality c)
  (+ (* 0.22 (translation-case-intent c))
     (* 0.22 (translation-case-control c))
     (* 0.18 (translation-case-edge c))
     (* 0.18 (translation-case-tests c))
     (* 0.20 (translation-case-maintain c))))

(displayln "case_name,translation_quality,warning")
(for ([c cases])
  (printf "~a,~a,Synthetic educational diagnostic only.~n"
          (translation-case-name c)
          (real->decimal-string (translation-quality c) 3)))
