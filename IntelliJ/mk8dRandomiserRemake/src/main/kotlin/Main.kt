fun main() {
	// the big lists
	val characters = arrayOf("Mario", "Luigi", "Peach", "Daisy", "Rosalina", "Tanooki Mario", "Cat Peach", "Yoshi", "Toad", "Koopa Troopa", "Shy Guy", "Lakitu", "Toadette", "King Boo", "Baby Mario", "Baby Luigi", "Baby Peach", "Baby Daisy", "Baby Rosalina", "Metal Mario", "Pink Gold Peach", "Wario", "Waluigi", "Donkey Kong", "Bowser", "Dry Bones", "Bowser Jr.", "Dry Bowser", "Lemmy", "Larry", "Wendy", "Ludwig", "Iggy", "Roy", "Morton", "Inkling Girl", "Inkling Boy", "Link", "Villager Boy", "Villager Girl", "Isabelle", "Mii", "Birdo", "Kamek", "Wiggler", "Petey Piranha")
	val kart = arrayOf("Standard Kart", "Pipe Frame", "Mach 8", "Steel Diver", "Cat Cruiser", "Circuit Special", "Tri-Speeder", "Badwagon", "Prancer", "Buggybud", "Landship", "Bounder", "Sports Coupé", "GLA", "W 25 Silver Arrow", "300 SL Roadster", "Blue Falcon", "Tanooki Kart", "B Dasher", "Streetle", "P-Wing", "Koopa Clown", "Standard Bike", "Comet", "Sport Bike", "The Duke", "Flame Rider", "Varmint", "Mr Scooty", "Jet Bike", "Yoshi Bike", "Master Cycle", "City Tripper", "Standard Quad", "Wild Wiggler", "Teddy Buggy", "Bone Rattler", "Splat Buggy", "Ink Striker")
	val wheels = arrayOf("Normal", "Monster", "Roller", "Slim", "Slick", "Metal", "Button", "Off-Road", "Sponge", "Wooden", "Cushion", "Normal Blue ", "Funky Monster", "Azure Roller", "Crimson Slim", "Cyber Slick", "Retro Off-Road", "GLA Wheels", "Triforce Tyres", "Ancient Tyres", "Leaf Tyres")
	val glider = arrayOf("Super Glider", "Cloud Glider", "Wario Wing", "Waddle Wing", "Peach Parasol", "Parachute", "Parafoil", "Flower Glider", "Bowser Kite", "Plane Glider", "MKTV Parafoil", "Hylian Kite", "Paraglider", "Paper Glider")
	val tracks = arrayOf("Mushroom Cup: Mario Kart Stadium",
		"Mushroom Cup: Water Park",
		"Mushroom Cup: Sweet Sweet Canyon",
		"Mushroom Cup: Thwomp Ruins",

		"Flower Cup: Mario Circuit",
		"Flower Cup: Toad Harbor",
		"Flower Cup: Twisted Mansion",
		"Flower Cup: Shy Guy Falls",

		"Star Cup: Sunshine Airport",
		"Star Cup: Dolphin Shoals",
		"Star Cup: Electrodome",
		"Star Cup: Mount Wario",

		"Special Cup: Cloudtop Cruise",
		"Special Cup: Bone Dry Dunes",
		"Special Cup: Bowser's Castle",
		"Special Cup: Rainbow Road",

		"Shell Cup: Moo Moo Meadows",
		"Shell Cup: Mario Circuit",
		"Shell Cup: Cheep Cheep Beach",
		"Shell Cup: Toad's Turnpike",

		"Banana Cup: Dry Dry Desert",
		"Banana Cup: Donut Plains 3",
		"Banana Cup: Royal Raceway",
		"Banana Cup: Dk Jungle",

		"Leaf Cup: Wario Stadium",
		"Leaf Cup: Sherbert Land",
		"Leaf Cup: Melody Motorway",
		"Leaf Cup: Yoshi Valley",

		"Lightning Cup: Tick-Tock Clock",
		"Lightning Cup: Piranha Plant Pipeway",
		"Lightning Cup: Grumble Volcano",
		"Lightning Cup: Rainbow Road",

		"Egg Cup: Yoshi Circuit",
		"Egg Cup: Excitebike Arena",
		"Egg Cup: Dragon Driftway",
		"Egg Cup: Mute City",

		"Triforce Cup: Wario's Gold Mine",
		"Triforce Cup: Rainbow Road",
		"Triforce Cup: Ice Ice Outpost",
		"Triforce Cup: Hyrule Circuit",

		"Crossing Cup: Baby Park",
		"Crossing Cup: Cheese Land",
		"Crossing Cup: Wild Woods",
		"Crossing Cup: Animal Crossing",

		"Bell Cup: Koopa City",
		"Bell Cup: Ribbon Road",
		"Bell Cup: Super Bell Subway",
		"Bell Cup: Big Blue",

		"Golden Dash Cup: Paris Promenade",
		"Golden Dash Cup: Toad Circuit",
		"Golden Dash Cup: Choco Mountain",
		"Golden Dash Cup: Coconut Mall",

		"Lucky Cat Cup: Tokyo Blur",
		"Lucky Cat Cup: Shroom Ridge",
		"Lucky Cat Cup: Sky Garden",
		"Lucky Cat Cup: Ninja Hideaway",

		"Turnip Cup: New York Minute",
		"Turnip Cup: Mario Circuit 3",
		"Turnip Cup: Kalimari Desert",
		"Turnip Cup: Waluigi Pinball",

		"Propeller Cup: Sidney Sprint",
		"Propeller Cup: Snow Land",
		"Propeller Cup: Mushroom Gorge",
		"Propeller Cup: Sky-High Sundae",

		"Rock Cup: London Loop",
		"Rock Cup: Boo Lake",
		"Rock Cup: Alpine Pass",
		"Rock Cup: Maple Treeway",

		"Moon Cup: Berlin Byways",
		"Moon Cup: Peach Gardens",
		"Moon Cup: Merry Mountain",
		"Moon Cup: Rainbow Road",

		"Fruit Cup: Amsterdam Drift",
		"Fruit Cup: Riverside Park",
		"Fruit Cup: DK's Snowboard Cross",
		"Fruit Cup: Yoshi's Island",

		"Boomerang Cup: Bangkok Rush",
		"Boomerang Cup: Mario Circuit",
		"Boomerang Cup: Waluigi Stadium",
		"Boomerang Cup: Singapore Speedway",

		"Feather Cup: Athens Dash",
		"Feather Cup: Daisy Cruiser",
		"Feather Cup: Moonview Highway",
		"Feather Cup: Squeaky Clean Sprint",

		"Cherry Cup: Los Angeles Laps",
		"Cherry Cup: Sunset Wilds",
		"Cherry Cup: Koopa Cape",
		"Cherry Cup: Vancouver Velocity")
	val dupes = mutableListOf<String>()

	println("Mario Kart 8 Deluxe Randomiser")
	println("Player 1:\n\tCharacter → ${characters.random()}\n\tKart → ${kart.random()}\n\tWheels → ${wheels.random()}\n\tGlider → ${glider.random()}")
	println("Player 2:\n\tCharacter → ${characters.random()}\n\tKart → ${kart.random()}\n\tWheels → ${wheels.random()}\n\tGlider → ${glider.random()}")
	println("Player 3:\n\tCharacter → ${characters.random()}\n\tKart → ${kart.random()}\n\tWheels → ${wheels.random()}\n\tGlider → ${glider.random()}")
	println("Player 4:\n\tCharacter → ${characters.random()}\n\tKart → ${kart.random()}\n\tWheels → ${wheels.random()}\n\tGlider → ${glider.random()}\n\n\n")

	for (i in 1..8) {
		var randomTrack = tracks.random()
		if (randomTrack in dupes) {
			randomTrack = tracks.random()
		}
		else {
			dupes.add(randomTrack)
			println(randomTrack)
		}

	}
}