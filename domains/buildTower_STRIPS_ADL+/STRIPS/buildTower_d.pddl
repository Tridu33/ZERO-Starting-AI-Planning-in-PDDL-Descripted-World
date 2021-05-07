(define (domain strips-blocksworld)
  (:requirements :strips)

  (:predicates
    (on ?x ?y) (clear ?x) (block ?x))

  (:action move
    :parameters (?b ?x ?y)
    :precondition (and (block ?b) (clear ?b) (on ?b ?x) (block ?y) (clear ?y))
    :effect (and (not (on ?b ?x)) (clear ?x)
  	       (not (clear ?y)) (on ?b ?y)))

  (:action move-to-table
    :parameters (?b ?x)
    :precondition (and (block ?b) (on ?b ?x) (clear ?b))
    :effect (and (not (on ?b ?x)) (clear ?x) (on ?b table)))
)
