#lang racket

(define path "input2.txt")

;;; Part 1

(define (submarine-position path)
  (with-input-from-file path
    (λ ()
      (let ([h-pos 0]
            [depth 0])
        (for ([l (in-lines)])
          (let* ([line (string-split l)]
                 [direction (car line)]
                 [value (string->number (last line))])
            (cond
              [(equal? "forward" direction) (set! h-pos (+ h-pos value))]
              [(equal? "down" direction) (set! depth (+ depth value))]
              [(equal? "up" direction) (set! depth (- depth value))])
            ))
        (* h-pos depth)))))

(submarine-position path)

;;; Part 2

(define (submarine-position2 path)
  (with-input-from-file path
    (λ ()
      (let ([h-pos 0]
            [depth 0]
            [aim 0])
        (for ([l (in-lines)])
          (let* ([line (string-split l)]
                 [direction (car line)]
                 [value (string->number (last line))])
            (cond
              [(equal? "forward" direction)
               (set! h-pos (+ h-pos value))
               (set! depth (+ depth (* aim value)))]
              [(equal? "down" direction) (set! aim (+ aim value))]
              [(equal? "up" direction) (set! aim (- aim value))])
            ))
        (* h-pos depth)))))

(submarine-position2 path)


