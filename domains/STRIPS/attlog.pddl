
;; STRIPS version of the ATT logistics domain and problems,
;; taken from the SGP distribution.

(define (domain logistics-strips)
  (:requirements :strips) 
  (:predicates 	(OBJ ?obj)
	       	(TRUCK ?truck)
               	(LOCATION ?loc)
		(AIRPLANE ?airplane)
                (CITY ?city)
                (AIRPORT ?airport)
		(at ?obj ?loc)
		(in ?obj1 ?obj2)
		(in-city ?obj ?city))

  (:action LOAD-TRUCK
    :parameters (?obj ?truck ?loc)
    :precondition (and (OBJ ?obj) (TRUCK ?truck) (LOCATION ?loc)
		       (at ?truck ?loc) (at ?obj ?loc))
    :effect (and (not (at ?obj ?loc)) (in ?obj ?truck))
    :duration 1)

  (:action LOAD-AIRPLANE
    :parameters (?obj ?airplane ?loc)
    :precondition (and (OBJ ?obj) (AIRPLANE ?airplane) (LOCATION ?loc)
		       (at ?obj ?loc) (at ?airplane ?loc))
    :effect (and (not (at ?obj ?loc)) (in ?obj ?airplane))
    :duration 1)

  (:action UNLOAD-TRUCK
    :parameters (?obj ?truck ?loc)
    :precondition (and (OBJ ?obj) (TRUCK ?truck) (LOCATION ?loc)
		       (at ?truck ?loc) (in ?obj ?truck))
    :effect (and (not (in ?obj ?truck)) (at ?obj ?loc))
    :duration 1)

  (:action UNLOAD-AIRPLANE
    :parameters (?obj ?airplane ?loc)
    :precondition (and (OBJ ?obj) (AIRPLANE ?airplane) (LOCATION ?loc)
		       (in ?obj ?airplane) (at ?airplane ?loc))
    :effect (and (not (in ?obj ?airplane)) (at ?obj ?loc))
    :duration 1)

  (:action DRIVE-TRUCK
    :parameters (?truck ?loc-from ?loc-to ?city)
    :precondition (and (TRUCK ?truck) (LOCATION ?loc-from) (LOCATION ?loc-to)
		       (CITY ?city) (in-city ?loc-from ?city) (in-city ?loc-to ?city)
		       (at ?truck ?loc-from))
    :effect (and (not (at ?truck ?loc-from)) (at ?truck ?loc-to))
    :duration 1)

  (:action FLY-AIRPLANE
    :parameters (?airplane ?loc-from ?loc-to)
    :precondition (and (AIRPLANE ?airplane) (AIRPORT ?loc-from) (AIRPORT ?loc-to)
		       (at ?airplane ?loc-from))
    :effect (and (not (at ?airplane ?loc-from)) (at ?airplane ?loc-to))
    :duration 1)
  )
