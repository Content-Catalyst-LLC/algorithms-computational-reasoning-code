#lang racket
(define (relative-improvement baseline heuristic) (/ (- baseline heuristic) baseline))
(displayln "test_name,value")
(displayln (format "route_improvement,~a" (relative-improvement 34 27)))
(displayln (format "annealing_improvement,~a" (relative-improvement 18.5 12.2)))
