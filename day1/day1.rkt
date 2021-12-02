#lang racket/base

(define path "input1.txt")

(define (delta-counter path)
  (with-input-from-file path
  (lambda ()
    (let ([curr (string->number (read-line))]
          [counter 0])
      (for ([l (in-lines)])
        (set! l (string->number l))
        (when (> l curr)
          (set! counter (add1 counter)))
        (set! curr l))
      counter))))

(delta-counter path)
