#lang racket
(define (branching-state-count b d) (for/sum ([i (in-range 0 (+ d 1))]) (expt b i)))
(define (ratio n d) (if (= d 0) 0 (/ n d)))
(displayln "test_name,value")
(displayln (format "branching_state_count,~a" (branching-state-count 3 5)))
(displayln "path_cost,11.5")
(displayln "heuristic_score,13.5")
(displayln (format "coverage_ratio,~a" (ratio 850 5000)))
(displayln (format "pruning_ratio,~a" (ratio 1200 4200)))
