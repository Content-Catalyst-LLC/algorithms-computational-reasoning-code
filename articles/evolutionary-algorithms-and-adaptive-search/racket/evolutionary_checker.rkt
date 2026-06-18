#lang racket
(define (binary-fitness xs) (apply + xs))
(displayln "test_name,value")
(displayln (format "binary_fitness,~a" (binary-fitness '(1 0 1 1))))
(displayln "mutation_rate,0.03")
