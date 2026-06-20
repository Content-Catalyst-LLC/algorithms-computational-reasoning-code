#lang racket
(define (density nodes edges)
  (if (<= nodes 1) 0 (/ edges (* nodes (- nodes 1)))))
(define (path-cost xs) (apply + xs))
(displayln "test_name,value")
(displayln "node_count,5")
(displayln "edge_count,7")
(displayln (format "density,~a" (density 5 7)))
(displayln (format "manual_shortest_path_cost,~a" (path-cost '(2.0 1.0 1.5 1.0))))
