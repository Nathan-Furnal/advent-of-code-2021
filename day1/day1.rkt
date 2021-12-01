#lang racket

(call-with-input-file "input1.txt"
  (lambda (in-port)
    (let loop ()
      (let ([data (read-line in-port)])
        (unless (eof-object? data)
          (displayln data)
          (loop))))))
