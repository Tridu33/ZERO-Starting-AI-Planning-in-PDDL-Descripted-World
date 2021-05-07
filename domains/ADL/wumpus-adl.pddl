
;; Wumpus World, ADL Version.
;;
;; This model uses several advanced features of PDDL: negative goals,
;; conditional effects and typing.
;;
;; An example problem is defined in wumpus-adl-1.pddl. Unfortunately,
;; this domain and/or problem seems to trigger a bug in IPP, which can
;; not solve it.

(define (domain wumpus-adl)
  (:requirements :adl :typing)

  ;; Here we define the five different types of object that will be
  ;; used. This replaces the static typing predicates used in the
  ;; STRIPS versions.
  (:types agent wumpus gold arrow square)

  (:predicates (at ?what ?square)
	       (adj ?square-1 ?square-2)
	       (pit ?square)
	       (have ?who ?what)
	       (alive ?who))

  ;; Using types, we can restrict the objects that may be used for
  ;; arguments to an action: Thus, the ?who argument of the "move"
  ;; action must be an object of type "agent" and the ?from and ?to
  ;; arguments must be objects of type "square".
  ;;
  ;; Note the weird syntax, in particular that there must be spaces
  ;; between the variable, hyphen and type name (since hyphens can
  ;; also be part of names in PDDL).
  (:action move
    :parameters (?who - agent ?from - square ?to - square)

    ;; The preconditions and unconditional effects of the "move" action
    ;; are the same as in the STRIPS version, except it does not forbid
    ;; the agent to move into a square containing either a pit or a live
    ;; wumpus. Instead, the action now have a set of conditional effects
    ;; that can change the truth value of the agents being "alive",
    ;; depending on what is in the ?to square.
    :precondition (and (alive ?who) (at ?who ?from) (adj ?from ?to))
    :effect (and (not (at ?who ?from)) (at ?who ?to)

		 ;; The syntax of a conditional effect is
		 ;;   (when <condition> <effect>)
		 ;; The meaning is that if the action is taken in a state
		 ;; where <condition> is true, the <effect> takes place,
		 ;; otherwise the effect has no effect.
		 ;;
		 ;; The first conditional effect specifies that if the
		 ;; ?to square is a pit, then (alive ?who) ceases to be
		 ;; true.
		 (when (pit ?to)
		   (and (not (alive ?who))))

		 ;; The second conditional effect has a more complicated
		 ;; condition, involving quantification. It reads "if there
		 ;; exists a wumpus ?w, such that ?w is in the ?to square
		 ;; and ?w is alive, then (alive ?who) ceases to be true".
		 (when (exists (?w - wumpus) (and (at ?w ?to) (alive ?w)))
		   (and (not (alive ?who)))))
    )

  ;; The "take" action presents us with a problem, since we want the agent
  ;; to be able to pick up objects of both types "gold" and "arrow". There
  ;; are several solutions:
  ;;
  ;; * Don't specify a type for the ?what parameter: To do this we can either
  ;;   place it last (if we write "?a ?b - foo", most planners will interpret
  ;;   this to mean parameters ?a and ?b are both of type "foo"), or by
  ;;   specifying the type of ?what to be "object" (the predefined "top-type").
  ;;   However, not all planners recognize object.
  ;;
  ;; * It is also possible to specify type heirarchies (in the :types part
  ;;   above), and using this we could create a type "thing" to be a supertype
  ;;   of both "gold" and "arrow". However, support for hierarchical types
  ;;   in current planners is weak, so most planners will not recognize them
  ;;   or will treat them incorrectly.
  ;;
  ;; * Use two different actions, "take-gold" and "take-arrow".
  ;;
  ;; Here, we've chosen the simple solution of not specifying a type for the
  ;; ?what parameter.
  (:action take
    :parameters (?who - agent ?where - square ?what)
    :precondition (and (alive ?who) (at ?who ?where) (at ?what ?where))
    :effect (and (have ?who ?what) (not (at ?what ?where)))
    )

  ;; The "shoot" action is similar to its STRIPS version. Note however that
  ;; we do not need to change any "dead" or "wumpus-in" predicates:since
  ;; using ADL features allows us to use complex preconditions (and goals),
  ;; we can specify "dead" as "not alive" and "wumpus-in" by the formula
  ;; in the second conditional effect of the "move" action.
  (:action shoot
    :parameters (?who - agent ?where - square ?with-arrow - arrow
		 ?victim - wumpus ?where-victim - square)
    :precondition (and (alive ?who)
		       (have ?who ?with-arrow)
		       (at ?who ?where)
		       (alive ?victim)
		       (at ?victim ?where-victim)
		       (adj ?where ?where-victim))
    :effect (and (not (alive ?victim))
		 (not (at ?victim ?where-victim))
		 (not (have ?who ?with-arrow)))
    )
)
