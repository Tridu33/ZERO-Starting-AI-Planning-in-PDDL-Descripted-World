;; Variation of the rockets domain in which rockets can be refuled
;; (making it even more like the plain logistics domain).
;; This domain (or one very similar) is in the graphplan distribution.

(define (domain refuel)
  (:requirements :strips)
  (:predicates
   (location ?x) (rocket ?x) (cargo ?x)
   (at ?t ?l) (in ?c ?r) (fuel ?r) (no-fuel ?r))

  (:action load
   :parameters (?c ?r ?l)
   :precondition (and (cargo ?c) (rocket ?r) (location ?l)
		      (at ?c ?l) (at ?r ?l))
   :effect (and (not (at ?c ?l)) (in ?c ?r)))

  (:action unload
   :parameters (?c ?r ?l)
   :precondition (and (cargo ?c) (rocket ?r) (location ?l)
		      (in ?c ?r) (at ?r ?l))
   :effect (and (not (in ?c ?r)) (at ?c ?l)))

  (:action fly
   :parameters (?r ?dep ?dst)
   :precondition (and (rocket ?r) (location ?dep) (location ?dst)
		      (at ?r ?dep) (not (= ?dep ?dst)) (fuel ?r))
   :effect (and (not (at ?r ?dep)) (at ?r ?dst) (not (fuel ?r))
		(no-fuel ?r)))

  (:action refuel
   :parameters (?r)
   :precondition (no-fuel ?r)
   :effect (and (fuel ?r) (not (no-fuel ?r))))
  )
