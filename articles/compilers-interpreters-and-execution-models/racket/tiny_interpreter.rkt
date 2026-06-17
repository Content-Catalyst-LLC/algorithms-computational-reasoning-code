#lang racket
(struct num (value))
(struct add (left right))
(struct mul (left right))
(define (eval-expr e)
  (cond [(num? e) (num-value e)]
        [(add? e) (+ (eval-expr (add-left e)) (eval-expr (add-right e)))]
        [(mul? e) (* (eval-expr (mul-left e)) (eval-expr (mul-right e)))]
        [else (error "unknown expression")]))
(displayln "expression,result")
(displayln (format "2 + 3 * 4,~a" (eval-expr (add (num 2) (mul (num 3) (num 4))))))
