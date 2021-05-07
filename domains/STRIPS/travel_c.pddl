;; Even simpler version of the "Travel" domain: No vehicles, just roads.

(define (domain travel)
  (:requirements :strips)
  (:predicates (road ?from ?to) (at ?thing ?location))

  (:action run
    :parameters (?person ?from ?to)
    :precondition (and (road ?from ?to)
		       (at ?person ?from)
		       (not (= ?from ?to)))
    :effect (and (at ?person ?to) (not (at ?person ?from))))
  )
