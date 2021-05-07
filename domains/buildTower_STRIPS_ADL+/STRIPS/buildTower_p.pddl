(define (problem strips-bw-1)
  (:domain strips-blocksworld)

  (:objects a b c table)

  (:init
     (on b table) (on a table) (on c a)
     (clear b) (clear c) (clear table)
     (block a) (block b) (block c))

  (:goal
     (and (on a b) (on b c) (on c table)))
)