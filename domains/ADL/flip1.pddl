
(define (problem flip1)
  (:domain flip)
  (:objects r1 r2 r3 - row c1 c2 c3 - column)
  (:init (white r2 c1))
  (:goal (forall (?r - row ?c - column) (white ?r ?c)))
  )
