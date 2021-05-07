
(define (problem springer_game)
  (:domain springer_game)
  (:objects x1 x2 x3 x4 x5 x6 x7 x8 y1 y2 y3 y4 y5 y6 y7 y8)
  (:init (inc x1 x2) (inc x2 x3) (inc x3 x4) (inc x4 x5) (inc x5 x6)
	 (inc x6 x7) (inc x7 x8) (dec x8 x7) (dec x7 x6) (dec x6 x5)
	 (dec x5 x4) (dec x4 x3) (dec x3 x2) (dec x2 x1)
	 (inc y1 y2) (inc y2 y3) (inc y3 y4) (inc y4 y5) (inc y5 y6)
	 (inc y6 y7) (inc y7 y8) (dec y8 y7) (dec y7 y6) (dec y6 y5)
	 (dec y5 y4) (dec y4 y3) (dec y3 y2) (dec y2 y1)
	 (mark x1 y1) (clear x1 y2) (clear x1 y3) (clear x1 y4)
	 (clear x1 y5) (clear x1 y6) (clear x1 y7) (clear x1 y8)
	 (clear x2 y1) (clear x2 y2) (clear x2 y3) (clear x2 y4)
	 (clear x2 y5) (clear x2 y6) (clear x2 y7) (clear x2 y8)
	 (clear x3 y1) (clear x3 y2) (clear x3 y3) (clear x3 y4)
	 (clear x3 y5) (clear x3 y6) (clear x3 y7) (clear x3 y8)
	 (clear x4 y1) (clear x4 y2) (clear x4 y3) (clear x4 y4)
	 (clear x4 y5) (clear x4 y6) (clear x4 y7) (clear x4 y8)
	 (clear x5 y1) (clear x5 y2) (clear x5 y3) (clear x5 y4)
	 (clear x5 y5) (clear x5 y6) (clear x5 y7) (clear x5 y8)
	 (clear x6 y1) (clear x6 y2) (clear x6 y3) (clear x6 y4)
	 (clear x6 y5) (clear x6 y6) (clear x6 y7) (clear x6 y8)
	 (clear x7 y1) (clear x7 y2) (clear x7 y3) (clear x7 y4)
	 (clear x7 y5) (clear x7 y6) (clear x7 y7) (clear x7 y8)
	 (clear x8 y1) (clear x8 y2) (clear x8 y3) (clear x8 y4)
	 (clear x8 y5) (clear x8 y6) (clear x8 y7) (clear x8 y8)
	 (at x1 y1))
  (:goal (and (mark x1 y1) (mark x1 y2) (mark x1 y3) (mark x1 y4)
	      (mark x1 y5) (mark x1 y6) (mark x1 y7) (mark x1 y8)
	      (mark x2 y1) (mark x2 y2) (mark x2 y3) (mark x2 y4)
	      (mark x2 y5) (mark x2 y6) (mark x2 y7) (mark x2 y8)
	      (mark x3 y1) (mark x3 y2) (mark x3 y3) (mark x3 y4)
	      (mark x3 y5) (mark x3 y6) (mark x3 y7) (mark x3 y8)
	      (mark x4 y1) (mark x4 y2) (mark x4 y3) (mark x4 y4)
	      (mark x4 y5) (mark x4 y6) (mark x4 y7) (mark x4 y8)
	      (mark x5 y1) (mark x5 y2) (mark x5 y3) (mark x5 y4)
	      (mark x5 y5) (mark x5 y6) (mark x5 y7) (mark x5 y8)
	      (mark x6 y1) (mark x6 y2) (mark x6 y3) (mark x6 y4)
	      (mark x6 y5) (mark x6 y6) (mark x6 y7) (mark x6 y8)
	      (mark x7 y1) (mark x7 y2) (mark x7 y3) (mark x7 y4)
	      (mark x7 y5) (mark x7 y6) (mark x7 y7) (mark x7 y8)
	      (mark x8 y1) (mark x8 y2) (mark x8 y3) (mark x8 y4)
	      (mark x8 y5) (mark x8 y6) (mark x8 y7) (mark x8 y8))))