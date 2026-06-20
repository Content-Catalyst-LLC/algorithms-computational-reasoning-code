#lang racket

(define data '((-2 -2.85) (-1 -0.67) (0 1.47) (1 3.63) (2 5.82)))

(define (predict w b x) (+ (* w x) b))
(define (mse w b)
  (/ (for/sum ([row data])
       (define x (first row))
       (define y (second row))
       (sqr (- y (predict w b x))))
     (length data)))

(define (step w b eta)
  (define n (length data))
  (define grad-w
    (for/sum ([row data])
      (define x (first row))
      (define y (second row))
      (* (/ 2 n) (- (predict w b x) y) x)))
  (define grad-b
    (for/sum ([row data])
      (define x (first row))
      (define y (second row))
      (* (/ 2 n) (- (predict w b x) y))))
  (values (- w (* eta grad-w)) (- b (* eta grad-b))))

(define-values (w b)
  (for/fold ([w 0.0] [b 0.0]) ([i (in-range 80)])
    (step w b 0.08)))

(displayln (list 'weight w 'bias b 'loss (mse w b)))
