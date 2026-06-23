#lang racket

(define text "THIS IS A TOY CLASSICAL CIPHER EXAMPLE")
(define counts (make-hash))
(for ([ch (in-string (string-downcase text))])
  (when (char-alphabetic? ch)
    (hash-update! counts ch add1 0)))
(displayln counts)
