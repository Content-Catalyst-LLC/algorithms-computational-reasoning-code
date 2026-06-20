#lang racket

(define (teaching-checksum s)
  (for/fold ([total 0]) ([ch (in-string s)] [i (in-naturals 1)])
    (modulo (+ total (* (char->integer ch) i)) 1000003)))

(define original "verified artifact manifest")
(define altered "verified artifact manifest!")
(printf "original checksum=~a\n" (teaching-checksum original))
(printf "altered checksum=~a\n" (teaching-checksum altered))
(printf "match=~a\n" (= (teaching-checksum original) (teaching-checksum altered)))
