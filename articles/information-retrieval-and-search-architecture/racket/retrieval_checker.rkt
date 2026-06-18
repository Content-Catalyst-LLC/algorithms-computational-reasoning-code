#lang racket
(define (precision tp retrieved) (if (= retrieved 0) 0 (/ tp retrieved)))
(define (recall tp relevant) (if (= relevant 0) 0 (/ tp relevant)))
(displayln "test_name,value")
(displayln (format "precision,~a" (precision 2 3)))
(displayln (format "recall,~a" (recall 2 2)))
