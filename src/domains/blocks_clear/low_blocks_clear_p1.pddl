(define (problem blockclear_problem) 
    (:domain blocks_clear)
    (:objects
        x y - BlockType)
    (:init
        (on_table A)
        (arm_empty)
        (on x A)
        (on y x)
        (clear y)
        ; (exists (?x - BlockType)
        ;     (or (above ?x A)
        ;         (== ?x A)))
    )
    (:goal (and
        (clear A)))
)
