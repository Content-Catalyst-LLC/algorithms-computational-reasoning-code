#lang racket

(struct profile (name step decomposition control testability representation governance) #:transparent)

(define profiles
  (list
   (profile "Recipe-like procedure" 86 72 70 62 42 20)
   (profile "Classroom algorithm exercise" 90 82 84 78 62 32)
   (profile "Search and ranking system" 72 70 76 66 78 70)
   (profile "Public decision-support workflow" 68 66 64 72 80 86)
   (profile "Scientific modeling workflow" 74 78 76 82 86 74)))

(define (algorithmic-score p)
  (+ (* 0.28 (profile-step p))
     (* 0.24 (profile-decomposition p))
     (* 0.24 (profile-control p))
     (* 0.24 (profile-testability p))))

(define (computational-score p)
  (+ (* 0.16 (profile-step p))
     (* 0.14 (profile-decomposition p))
     (* 0.14 (profile-control p))
     (* 0.14 (profile-testability p))
     (* 0.22 (profile-representation p))
     (* 0.20 (profile-governance p))))

(displayln "name,algorithmic_score,computational_score,warning")
(for ([p profiles])
  (printf "~a,~a,~a,Synthetic educational diagnostic only.~n"
          (profile-name p)
          (real->decimal-string (algorithmic-score p) 3)
          (real->decimal-string (computational-score p) 3)))
