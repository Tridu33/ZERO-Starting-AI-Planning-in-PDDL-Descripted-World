;; The Molgen domain, in an almost plain STRIPS version (adapted from
;; the SGP problem set).

;; The original problem had an existentially quantified goal, which is
;; here circumvented using a substitute predicate "construct-solved" and
;; an action "solve-construct" to choose the satisfying objects (as
;; parameters).

;; I'm not sure what the point of the constant "linker" is (maybe because
;; I don't know too much about genetics ;) It's only used in an inequality
;; in the preconditions of the actions "ligate1" and "ligate2", so it can
;; probably be removed without really affecting the problem.

(define (domain molgen-strips)
  (:requirements :strips :equality)
  (:constants linker)
  (:predicates
   (mRNA ?x) (molecule ?x) (connected-cDNA-mRNA ?x)
   (bacterium ?x) (antibiotic ?x)
   (single-strand ?x) (hair-pin ?x) (double-strand ?x)
   (cleavable ?x) (cleaved ?x) (pure ?x)
   (accepts ?x ?y) (contains ?x ?y) (resists ?x ?y)
   ;; the construct-solved predicate used to circumvent the
   ;; need for an existential quantifier in the problem goal
   (construct-solved ?z))

  (:action reverse-transcribe
    :parameters (?x)
    :precondition (mRNA ?x)
    :effect (connected-cDNA-mRNA ?x))

  (:action separate
    :parameters (?x)
    :precondition (connected-cDNA-mRNA ?x)
    :effect (and (single-strand ?x) (not (connected-cDNA-mRNA ?x))))

  (:action polymerize
    :parameters (?x)
    :precondition (single-strand ?x)
    :effect (and (hair-pin ?x) (not (single-strand ?x))))

  (:action digest
    :parameters (?x)
    :precondition (hair-pin ?x)
    :effect (and (double-strand ?x) (hair-pin ?x)))

  ;; splicing DNA molecules
  (:action ligate1
    :parameters (?y)
    :precondition (and (double-strand ?y) (not (= ?y linker)))
    :effect (cleavable ?y))

  (:action ligate2
    :parameters (?y ?x)
    :precondition (and (cleaved ?x) (cleaved ?y) (not (= ?x linker)))
    :effect (and (contains ?x ?y) (cleavable ?y)
		 (not (cleaved ?x)) (not (cleaved ?y))))

  (:action cleave
    :parameters (?x)
    :precondition (cleavable ?x)
    :effect (and (cleaved ?x) (not (cleavable ?x))))

  ;; inserting a molecule into an organism
  (:action transform
    :parameters (?x ?y)
    :precondition (and (bacterium ?y)
		       (cleavable ?x)    ; molecule must be whole
		       (accepts ?x ?y)   ; is molecule accepted?
		       (not (= ?x ?y)))
    :effect (and (contains ?x ?y) (not (cleavable ?x))))

  ;; purify a culture with an antibiotic
  (:action screen
    :parameters (?x ?y ?z)
    :precondition (and (bacterium ?x) (antibiotic ?z)
		       (resists ?z ?y) (contains ?y ?x)
		       (not (= ?x ?y)) (not (= ?y ?z)) (not (= ?x ?z)))
    :effect (pure ?x))

  ;; the solve-construct action "encodes" an existential quantifier
  ;; over ?x and ?y:
  (:action solve-construct
    :parameters (?x ?y ?z)
    :precondition (and (bacterium ?y) (molecule ?x) (contains ?z ?x)
		       (contains ?x ?y) (pure ?y))
    :effect (construct-solved ?z))
  )
