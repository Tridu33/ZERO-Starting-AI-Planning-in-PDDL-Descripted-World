
(define (domain blocks_clear_d)
    (:requirements :typing :non-deterministic)
    (:types	)
    (:predicates
    (vStart)
    (vGoal)
    (BlocksCleared)
    (H)
    )
    
    (:action 8_virtual_source_act_0
    :parameters ()
        :precondition (and  (vStart)  )
        :effect (and (not(vStart)) (not(vGoal)) (not(BlocksCleared)) (not(H)) )
    )
    (:action 0_unstack_1_7
            :parameters ()
        :precondition (and (not(vStart)) (not(vGoal)) (not(BlocksCleared)) (not(H)) )
        :effect (oneof 
        (and (not(vStart)) (not(vGoal)) (not(BlocksCleared)) (H) )
        (and (not(vStart)) (vGoal) (BlocksCleared) (H) )
        )
    )
    (:action 1_putdown_0
            :parameters ()
        :precondition (and (not(vStart)) (not(vGoal)) (not(BlocksCleared)) (H) )
        :effect (and (not(vStart)) (not(vGoal)) (not(BlocksCleared)) (not(H)) )
    )
)