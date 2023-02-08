Beer application

Short description:

Projekt o pivima sluzi za informiranje o pivima te ocijenjivanje i komentiranje istih. 
projket bi pratio vise vrdsta piva iz vise pivovara, za svaku vrstu piva(pale ale, lager, pils..)
i za svaku pivovaru(medvedgrad, osjecka..) je moguće ostaviti subjektivno misljenje uz ocijenu. 
Moguce je i procitati sastav piva te kakav je okus tekstura, aftertaste i tako dalje.
komentari i ocjene konzumenata uz cinjenice ce dati svakom korisniku pravu predođbu i sliku piva koje ga zanima. 
Strancica se moze filtrirati po proizvodacu ili vrsti piva.
može se pretraživati željeno pivo po nazivu ili vrsti
Što bi znacilo ukolikko vas zanima vrsta piva dobili biste listu piva te vrste iz svih pivovara,
a ukoliko se zelite usredotociti na samo jednog proizvodaca vidjeli biste sva piva koje taj proizvodac nudi.


MODELS:

		manufacture
				-ID
				-name
				-adress
				-town
				-postal code

		beer_type
				-ID
				-name
				-description

		beer
			-ID
			-beer_type_id
			-manufacture_id
			-name
			-alcohol_precentage
			-color
			-aroma(bitter,sweet,sour,bitter sour,bitter sweet,sweet sour, no aroma)
			-water
			-barley(ječam)
			-hop(hmelj)
			-yeast(kvasac)
			
		review
			-id
			-beer__id
			-grade
			-description
			
		
		+ambalaža
		
		