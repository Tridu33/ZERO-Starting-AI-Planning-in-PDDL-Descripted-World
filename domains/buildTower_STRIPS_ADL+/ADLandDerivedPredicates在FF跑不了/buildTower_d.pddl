;This example uses derived predicates to infer the value of the clear predicate, instead of having to keep track of its value manually through the action as in the previous ADL example.
(define (domain der-adl-blocksworld)
  (:requirements :adl :derived-predicates)
  (:types block )
  ;(:constants    )
  (:predicates (on ?x ?y)(clear ?x))
  (:derived (clear ?x) (or (= ?x table)
 	                   (not (exists (?y - block) (on ?y ?x)))))

  (:action move
     :parameters (?b - block ?x ?y)
     :precondition (and (clear ?b) (on ?b ?x) (clear ?y))
     :effect (and (on ?b ?y)
     	     	  (not (on ?b ?x)))
  )
)








