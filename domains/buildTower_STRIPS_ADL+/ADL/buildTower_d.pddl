;The same Blocks World, but implemented using ADL features. It uses typing to get rid of the unary block predicate and conditional effects to integrate both move actions of the STRIPS example into a single action.



(define (domain adl-blocksworld)
  (:requirements :adl)
  (:types block)
  (:predicates (on ?x ?y) (clear ?x))

  (:action move
     :parameters (?b - block ?x ?y)
     :precondition (and
     		    (clear ?b) (on ?b ?x) (clear ?y))
     :effect (and (on ?b ?y)
     	     	  (not (on ?b ?x))
		  (clear ?x)
		  (when (not (= ?y table))
		  	(not (clear ?y))))
  )
)























