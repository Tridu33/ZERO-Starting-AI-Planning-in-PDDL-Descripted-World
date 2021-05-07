(define (problem rocket_a)
  (:domain refuel)
  (:objects
   London Paris JFK BOS R1 R2 mxf avrim alex jason pencil paper april
   michelle betty lisa)
  (:init
   (location London) (location Paris) (location JFK) (location BOS)
   (rocket R1) (rocket R2) (cargo mxf) (cargo avrim) (cargo alex)
   (cargo jason) (cargo pencil) (cargo paper) (cargo april) (cargo michelle)
   (cargo betty) (cargo lisa)
   (at R1 JFK) (at R2 BOS) (fuel R1) (fuel R2) (at mxf Paris) (at avrim Paris)
   (at alex Paris) (at jason JFK) (at pencil London) (at paper London)
   (at michelle London) (at april London) (at betty London) (at lisa London))
  (:goal (and (at mxf BOS) (at avrim JFK) (at pencil BOS) (at alex JFK)
	      (at april BOS) (at lisa Paris) (at michelle JFK) (at jason BOS)
	      (at paper Paris) (at betty JFK)))
  )
