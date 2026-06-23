#lang racket

(define (run-feedback n target gain x)
  (if (= n 0)
      x
      (run-feedback (- n 1) target gain (- x (* gain (- x target))))))

(displayln (format "final_state=~a" (run-feedback 5 0.0 0.2 10.0)))
