(define (problem der-adl-blocksworld-problem)
  (:domain der-adl-blocksworld)
  (:objects a b c - block table)

  (:init
     (on b table) (on a table) (on c a)
  )

  (:goal
     (and (on a b) (on b c) (on c table)))
)