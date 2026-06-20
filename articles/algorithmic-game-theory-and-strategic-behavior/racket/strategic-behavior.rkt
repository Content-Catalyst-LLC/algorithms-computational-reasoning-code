#lang racket
(define profiles '((cooperate cooperate 3 3) (cooperate defect 0 5) (defect cooperate 5 0) (defect defect 1 1)))
(for ([p profiles]) (match p [(list p1 p2 u1 u2) (printf "~a/~a welfare=~a\n" p1 p2 (+ u1 u2))]))
