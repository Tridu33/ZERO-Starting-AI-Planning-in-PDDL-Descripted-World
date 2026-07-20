(define (domain trees_alt)
	(:requirements :typing)
	(:types
		variable node
	)
	(:predicates
		; tree information
		(left-child ?child ?parent - node)
		(right-child ?child ?parent - node)
		(internal ?node - node)
		(visited ?node - node)

		; variables
		(assignment ?var - variable ?node - node)
		; (isinternal ?var - variable)
	)

	;assign(cur,cur->left), a.k.a: "cur = cur->left"
	(:action copy-left
		:parameters (?var1 ?var2 - variable ?child ?parent - node)
		:precondition (and 
			(assignment ?var1 ?parent)
			(left-child ?child ?parent)
			(not (assignment ?var2 ?node))
			)
		:effect (and (assignment ?var2 ?child))
	)

	;assign(cur,cur->right), a.k.a: "cur = cur->right"
	(:action copy-right
		:parameters (?var1 ?var2 - variable ?child ?parent - node)
		:precondition (and 
			(assignment ?var1 ?parent)
			(right-child ?child ?parent)
			(not (assignment ?var2 ?node)))
		:effect (and(assignment ?var2 ?child))
		; :effect (and( If you take the inverse memory and only keep one memory predicate, you can't access the right side after accessing the left side not(assignment ?var1 ?parent))(assignment ?var2 ?child))
	)

	(:action visit
		:parameters (?var - variable ?node - node)
		:precondition (and (assignment ?var ?node))
		:effect (and (visited ?node))
	)


)