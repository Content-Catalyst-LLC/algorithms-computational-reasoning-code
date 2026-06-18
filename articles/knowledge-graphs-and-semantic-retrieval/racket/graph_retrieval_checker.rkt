#lang racket
(define (hybrid-score l v g p) (* 100 (+ (* .25 l) (* .25 v) (* .25 g) (* .25 p))))
(define (path-score path-length confidence provenance review)
  (define length-factor (/ 1 (+ 1 (max (- path-length 1) 0))))
  (* 100 (+ (* .25 length-factor) (* .30 confidence) (* .30 provenance) (* .15 review))))
(displayln "test_name,value")
(displayln (format "hybrid_score,~a" (hybrid-score .82 .78 .88 .90)))
(displayln (format "graph_path_score,~a" (path-score 3 .90 .92 .95)))
