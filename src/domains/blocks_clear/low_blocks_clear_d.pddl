; ADD (transitive_closure (above,on))
; means:predicate 'above' is transitive_closure of predicate 'on'.
; will be used in describe high level action with low level language 
(define (domain blocks_clear)
  (:requirements :strips :equality :typing  :derived-predicates);:transitive_closure)
  (:types BlockType)
  (:constants
    A - BlockType
  )
  (:predicates 
            (arm_empty)
            (clear ?x - BlockType)
            (on_table ?x - BlockType)
            (holding ?x - BlockType)
            (on ?x ?y - BlockType)
            ;;;;;;;;;;;;;;;
            (vStart)
            (VGoal)
            (BlocksCleared)
            (H)
            ; (nBiggerThan0)
            )
  ;(:transitive_closure (above,on)); 
  (:derived
        (BlocksCleared)
        (clear A))
    (:derived
        (H)
        (exists (?x - BlockType) (holding ?x)))
    ; (:derived
    ;     (nBiggerThan0)
    ;     (exists (?x - BlockType) (above ?x A)))
  ; (:action pickup
  ;   :parameters (?x - BlockType)
  ;   :precondition (and (clear ?x) (on_table ?x) (arm_empty))
  ;   :effect (and (holding ?x) (not (clear ?x)) (not (on_table ?x)) 
  ;                (not (arm_empty))))

  (:action putdown
    :parameters  (?x - BlockType)
    :precondition (holding ?x)
    :effect (and (clear ?x) (arm_empty) (on_table ?x) 
                (not (holding ?x))))

  ; (:action stack
  ;   :parameters  (?x ?y - BlockType)
  ;   :precondition (and (clear ?y) (holding ?x))
  ;   :effect (and (arm_empty) (clear ?x) (on ?x ?y)
  ;               (not (clear ?y)) (not (holding ?x))))

  (:action unstack
    :parameters  (?x ?y - BlockType)
    :precondition (and (on ?x ?y) (clear ?x) (arm_empty))
    :effect (and (holding ?x) (clear ?y)
                (not (on ?x ?y)) (not (clear ?x)) (not (arm_empty))))
  
  (:formula_for_initial_states
      (and
        (arm_empty)
        (not (clear A))
      )
  )
  (:formula_for_goals 
    (and
      (clear A))
  )
)











