#lang racket/base
(require data/queue)

(define path "input1.txt")

(define (window-counter path window-size)
  (with-input-from-file path
    (lambda ()
      (let ([queue (make-queue)]
            [counter 0])
        (for ([i (in-range window-size)])
          (enqueue! queue (string->number (read-line))))
        (let ([curr (dequeue! queue)])
          (for ([l (in-lines)])
            [set! l (string->number l)]
            [when (> l curr)
              (set! counter (add1 counter))]
            (enqueue! queue l)
            (set! curr (dequeue! queue))))
        counter))))

(window-counter path 3)
