#lang racket

(struct scenario (name representation correctness governance brute-force) #:transparent)

(define scenarios
  (list
   (scenario "Brute-force procedure" 40 28 20 92)
   (scenario "Indexed search design" 62 52 38 42)
   (scenario "Graph-aware reasoning" 76 68 54 30)
   (scenario "Governed computational reasoning" 86 82 86 18)))

(define (clamp x) (max 0 (min 100 x)))

(define (reasoning-score s)
  (clamp (- (+ (* 0.30 (scenario-representation s))
               (* 0.30 (scenario-correctness s))
               (* 0.30 (scenario-governance s)))
            (* 0.10 (scenario-brute-force s)))))

(displayln "scenario,reasoning_score,warning")
(for ([s scenarios])
  (printf "~a,~a,Synthetic governance diagnostic only.~n"
          (scenario-name s)
          (real->decimal-string (reasoning-score s) 3)))
