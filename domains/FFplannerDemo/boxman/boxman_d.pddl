(define (domain boxman)
  (:requirements :strips :typing:equality
                 :universal-preconditions
                 :conditional-effects)
  (:types loc)
  (:predicates
      (boxAt ?y - loc)
      (manAt ?y - loc)
      (adjacent ?x - loc ?y -loc) 
      (notClear ?x - loc)
      (line ?x ?y ?z -loc)
      )   

	(:action push
	:parameters(?mp ?bp ?np - loc ?)
	:precondition(and (manAt ?mp)(boxAt ?bp)(not (notClear ?np))(line ?mp ?bp ?np))
        :effect(and (not (notClear ?mp))(notClear ?np)
                    (not (manAt ?mp))(manAt ?bp)
                    (not (boxAt ?bp))(boxAt ?np)
        )
	)

	(:action move
        :parameters(?x ?y - loc)
        :precondition(and (manAt ?x)(not (notClear ?y))(adjacent ?x ?y) )
        :effect(and (not (manAt ?x))(manAt ?y)
                    (not (notClear ?x))(notClear ?y)
        )
	)


)