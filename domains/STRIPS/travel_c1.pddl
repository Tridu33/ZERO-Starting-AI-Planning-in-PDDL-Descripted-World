(define (problem hit-the-road-jack)
  (:domain travel)
  (:objects jack microsoft rockwell KI)
  (:init (at jack rockwell)
	 (road rockwell KI)
	 (road KI microsoft))
  (:goal (at jack microsoft))
  )
