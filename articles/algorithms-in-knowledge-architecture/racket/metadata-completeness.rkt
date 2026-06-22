#lang racket

(define present-fields 11.0)
(define required-fields 12.0)
(define score (/ present-fields required-fields))
(displayln (format "metadata_completeness_score=~a" score))
