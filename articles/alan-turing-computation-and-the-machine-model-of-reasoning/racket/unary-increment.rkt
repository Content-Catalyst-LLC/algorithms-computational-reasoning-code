#lang racket

(define (unary-increment tape)
  (let loop ([chars (string->list tape)] [acc '()])
    (cond
      [(empty? chars) (list->string (reverse (append (list #\_ #\1) acc)))]
      [(char=? (first chars) #\1) (loop (rest chars) (cons #\1 acc))]
      [(char=? (first chars) #\_) (list->string (reverse (append (list #\_ #\1) acc)))]
      [else tape])))

(displayln (format "incremented_tape=~a" (unary-increment "111_")))
