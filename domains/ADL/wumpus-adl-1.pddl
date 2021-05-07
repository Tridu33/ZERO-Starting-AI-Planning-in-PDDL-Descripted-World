
;; This is a problem definition for the ADL version of the Wumpus
;; World (see wumpus-adl.pddl).

(define (problem wumpus-adl-1)
  (:domain wumpus-adl)
  (:objects

   ;; Since this version of the domain uses typing, we have to
   ;; specify the type of each object.
   s-1-1 s-1-2 s-1-3 s-2-1 s-2-2 s-2-3 - square
   gold-1 - gold
   arrow-1 - arrow
   agent-1 - agent
   wumpus-1 - wumpus)
  (:init (adj s-1-1 s-1-2) (adj s-1-2 s-1-1)
	 (adj s-1-2 s-1-3) (adj s-1-3 s-1-2)
	 (adj s-2-1 s-2-2) (adj s-2-2 s-2-1)
	 (adj s-2-2 s-2-3) (adj s-2-3 s-2-2)
	 (adj s-1-1 s-2-1) (adj s-2-1 s-1-1)
	 (adj s-1-2 s-2-2) (adj s-2-2 s-1-2)
	 (adj s-1-3 s-2-3) (adj s-2-3 s-1-3)
	 (pit s-1-2)
	 (at gold-1 s-1-3)
	 (at agent-1 s-1-1)
	 (alive agent-1)
	 (have agent-1 arrow-1)
	 (at wumpus-1 s-2-3)
	 (alive wumpus-1))

  ;; We add to the goal the condition that the agent should be still
  ;; be alive at the end of the plan. This, combined with the conditional
  ;; effects of the "move" action, will cause the planner to avoid
  ;; unintended moves (such as into a pit or a wumpus lair).
  (:goal (and (have agent-1 gold-1) (at agent-1 s-1-1) (alive agent-1)))
  )
