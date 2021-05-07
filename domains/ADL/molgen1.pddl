;; Molgen's rat insulin problem (ADL version).

(define (problem rat-insulin-adl)
  (:domain molgen-adl)
  (:objects insulin-gene e-coli-exosome junk-exosome
	    e-coli junk antibiotic-1)
  (:init (molecule insulin-gene)
	 (molecule e-coli-exosome)
	 (molecule junk-exosome) (molecule linker)
	 (bacterium e-coli) (bacterium junk)
	 (antibiotic antibiotic-1)
	 (mRNA insulin-gene)
	 (cleavable e-coli-exosome)
	 (cleavable junk-exosome)
	 (accepts junk-exosome junk)
	 (accepts e-coli-exosome e-coli)
	 (resists antibiotic-1 e-coli-exosome))
  (:goal (exists (?y ?x)
		 (and (bacterium ?y) 
		      (molecule ?x)
		      (contains insulin-gene ?x)
		      (contains ?x ?y)
		      (pure ?y))))
  ;; For planners that do not support existentially quantified goals,
  ;; one can cheat a bit and use the following goal instead:
  ;;  (:goal (and (contains insulin-gene e-coli-exosome)
  ;;	      (contains e-coli-exosome e-coli)
  ;;	      (pure e-coli)))
  )
