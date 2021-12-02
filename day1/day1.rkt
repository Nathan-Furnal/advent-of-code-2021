#lang racket/base

(define path "input1.txt")

(call-with-input-file path
  (lambda (in-port)
    (let loop ()
      (let ([data (read-line in-port)])
        (unless (eof-object? data)
          (displayln data)
          (loop))))))


(call-with-input-file path
  (lambda (in-port)
    (let loop ()
      (let ([curr (string->number (read-line in-port))]
            [next (string->number (peek-string 1 0 in-port))])
        (unless (eof-object? next)
          (cond
            [(> next curr) (display curr)])
          (loop))))))


