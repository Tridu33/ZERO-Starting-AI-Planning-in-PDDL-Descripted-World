;One particular oddity of the move action in the ADL example is that it requires three parameters. The two obvious parameters are the block to move, and its destination. Maybe unexpectedly, another parameter is required, and that is the block that is underneath the block that is to be moved. This is to unset the on predicate that describes the current situation of block b on block x before the move. Since this block x can be derived from the data, it would feel natural if it is not required as a parameter and instead could be queried in the precondition. This program tests whether this is supported.


(define (domain precond-adl-blocksworld)
  (:requirements :adl)
  (:types block)
  (:predicates (on ?x ?y) (clear ?x))

  (:action move
; notice the use of only two parameters, the parameter
; ?x is bound in the precondition.
     :parameters (?b - block ?y)
     :precondition (exists (?x) (and
     		    (clear ?b) (on ?b ?x) (clear ?y)))
     :effect (and (on ?b ?y)
     	     	  (not (on ?b ?x))
		  (clear ?x)
		  (when (not (= ?y table))
		  	(not (clear ?y))))
  )
)








