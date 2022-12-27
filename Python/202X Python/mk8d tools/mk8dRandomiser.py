# import packages
from random import choice
import pandas as pd

# the big bois
character = [
		'Mario',
		'Luigi',
		'Peach',
		'Daisy',
		'Rosalina',
		'Tanooki Mario',
		'Cat Peach',
		'Yoshi',
		'Toad',
		'Koopa Troopa',
		'Shy Guy',
		'Lakitu',
		'Toadette',
		'King Boo',
		'Baby Mario',
		'Baby Luigi',
		'Baby Peach',
		'Baby Daisy',
		'Baby Rosalina',
		'Metal Mario',
		'Pink Gold Peach',
		'Wario',
		'Waluigi',
		'Donkey Kong',
		'Bowser',
		'Dry Bones',
		'Bowser Jr.',
		'Dry Bowser',
		'Lemmy',
		'Larry',
		'Wendy',
		'Ludwig',
		'Iggy',
		'Roy',
		'Morton',
		'Inkling Girl',
		'Inkling Boy',
		'Link',
		'Villager Boy',
		'Villager Girl',
		'Isabelle',
		'Mii',
	]
kart = [
		'Standard Kart',
		'Pipe Frame',
		'Mach 8',
		'Steel Diver',
		'Cat Cruiser',
		'Circuit Special',
		'Tri-Speeder',
		'Badwagon',
		'Prancer',
		'Buggybud',
		'Landship',
		'Bounder',
		'Sports Coupé',
		'GLA',
		'W 25 Silver Arrow',
		'300 SL Roadster',
		'Blue Falcon',
		'Tanooki Kart',
		'B Dasher',
		'Streetle',
		'P-Wing',
		'Koopa Clown',
		'Standard Bike',
		'Comet',
		'Sport Bike',
		'The Duke',
		'Flame Rider',
		'Varmint',
		'Mr Scooty',
		'Jet Bike',
		'Yoshi Bike',
		'Master Cycle',
		'City Tripper',
		'Standard Quad',
		'Wild Wiggler',
		'Teddy Buggy',
		'Bone Rattler',
		'Splat Buggy',
		'Ink Striker',
	]
wheels = [
		'Normal',
		'Monster',
		'Roller',
		'Slim',
		'Slick',
		'Metal',
		'Button',
		'Off-Road',
		'Sponge',
		'Woodden',
		'Cushion',
		'Normal Blue ',
		'Funky Monster',
		'Azure Roller',
		'Crimson Slim',
		'Cyber Slick',
		'Retro Off-Road',
		'GLA Wheels',
		'Triforce Tyres',
		'Ancient Tyres',
		'Leaf Tyres'
	]
glider = [
		'Super Glider',
		'Cloud Glider',
		'Wario Wing',
		'Waddle Wing',
		'Peach Parasol',
		'Parachute',
		'Parafoil',
		'Flower Glider',
		'Bowser Kite',
		'Plane Glider',
		'MKTV Parafoil',
		'Hylian Kite',
		'Paraglider',
		'Paper Glider',
	]
track = [
		'Mushroom Cup: Mario Kart Stadium',
		'Mushroom Cup: Water Park',
		'Mushroom Cup: Sweet Sweet Canyon',
		'Mushroom Cup: Thwomp Ruins',

		'Flower Cup: Mario Circuit',
		'Flower Cup: Toad Harbor',
		'Flower Cup: Twisted Mansion',
		'Flower Cup: Shy Guy Falls',

		'Star Cup: Sunshine Airport',
		'Star Cup: Dolphin Shoals',
		'Star Cup: Electrodome',
		'Star Cup: Mount Wario',

		'Special Cup: Cloudtop Cruise',
		'Special Cup: Bone Dry Dunes',
		'Special Cup: Bowser\'s Castle',
		'Special Cup: Rainbow Road',

		'Shell Cup: Moo Moo Meadows',
		'Shell Cup: Mario Circuit',
		'Shell Cup: Cheep Cheep Beach',
		'Shell Cup: Toad\'s Turnpike',

		'Banana Cup: Dry Dry Desert',
		'Banana Cup: Donut Plains 3',
		'Banana Cup: Royal Raceway',
		'Banana Cup: Dk Jungle',

		'Leaf Cup: Wario Stadium',
		'Leaf Cup: Sherbert Land',
		'Leaf Cup: Melody Motorway',
		'Leaf Cup: Yoshi Valley',

		'Lightning Cup: Tick-Tock Clock',
		'Lightning Cup: Piranha Plant Pipeway',
		'Lightning Cup: Grumble Volcano',
		'Lightning Cup: Rainbow Road',

		'Egg Cup: Yoshi Ciruit',
		'Egg Cup: Excitebike Arena',
		'Egg Cup: Dragon Driftway',
		'Egg Cup: Mute City',

		'Triforce Cup: Wario\'s Gold Mine',
		'Triforce Cup: Rainbow Road',
		'Triforce Cup: Ice Ice Outpost',
		'Triforce Cup: Hyrule Circuit',

		'Crossing Cup: Baby Park',
		'Crossing Cup: Cheese Land',
		'Crossing Cup: Wild Woods',
		'Crossing Cup: Animal Crossing',

		'Bell Cup: Koopa City',
		'Bell Cup: Ribbon Road',
		'Bell Cup: Super Bell Subway',
		'Bell Cup: Big Blue',

		'Golden Dash Cup: Paris Promenade',
		'Golden Dash Cup: Toad Circuit',
		'Golden Dash Cup: Choco Mountain',
		'Golden Dash Cup: Coconut Mall',

		'Lucky Cat Cup: Tokyo Blur',
		'Lucky Cat Cup: Shroom Ridge',
		'Lucky Cat Cup: Sky Garden',
		'Lucky Cat Cup: Ninja Hideaway',

		'Turnip Cup: New York Minute',
		'Turnip Cup: Mario Circuit 3',
		'Turnip Cup: Kalimari Desert',
		'Turnip Cup: Waluigi Pinball',

		'Propeller Cup: Sidney Sprint',
		'Propeller Cup: Snow Land',
		'Propeller Cup: Mushroom Gorge',
		'Propeller Cup: Sky-High Sundae',

		'Rock Cup: London Loop',
		'Rock Cup: Boo Lake',
		'Rock Cup: Alpine Pass',
		'Rock Cup: Maple Treeway',

		'Moon Cup: Berlin Byways',
		'Moon Cup: Peach Gardens',
		'Moon Cup: Merry Mountain',
		'Moon Cup: Rainbow Road'
	]


# Custom Cups

CUSTOMdoubleFoodCup = [
	'Mushroom Cup: Sweet Sweet Canyon',
	'Crossing Cup: Cheese Land',
	'Leaf Cup: Sherbet Land',
	'Golden Dash Cup: Choco Mountain',
	'Turnip Cup: Kalimari Desert',
	'Propeller Cup: Mushroom Gorge',
	'Propeller Cup: Sky High Sundae'
	'Rock Cup: Maple Treeway'
	]

CUSTOMsingleCups = []

CUSTOMsingleWaterCup = {
	"Name": 'Water Cup',
	"Track 1": 'Mushroom Cup: Water Park',
	"Track 2": 'Star Cup: Dolphin Shoals',
	"Track 3": 'Shell Cup: Cheep Cheep Beach',
	"Track 4": 'Rock Cup: Boo Lake'
}
CUSTOMsingleCups.append(CUSTOMsingleWaterCup) # i couldn't think of a neater way to this i'm so sorry if anyone finds this please lmk a better way

CUSTOMsingleDesertCup = {
	"Name": 'Desert Cup',
	"Track 1": 'Banana Cup: Dry Dry Desert',
	"Track 2": 'Crossing Cup: Cheese Land',
	"Track 3": 'Special Cup: Bone Dry Dunes',
	"Track 4": 'Turnip Cup: Kalimari Desert'
}
CUSTOMsingleCups.append(CUSTOMsingleDesertCup)

CUSTOMsingleIceCup = {
	"Name": 'Ice Cup',
	"Track 1": 'Crossing Cup: Animal Crossing (Winter ZR)',
	"Track 2":'Leaf Cup: Sherbet Land',
	"Track 3": 'Triforce Cup: Ice Ice Outpost',
	"Track 4": 'Propeller Cup: Snow Land'
	}
CUSTOMsingleCups.append(CUSTOMsingleIceCup)

CUSTOMsingleForestCup = {
	"Name": 'Forest Cup',
	"Track 1": 'Banana Cup: DK Jungle',
	"Track 2": 'Mushroom Cup: Thwomp Ruins',
	"Track 3": 'Crossing Cup: Wild Woods',
	"Track 4": 'Rock Cup: Maple Treeway'
}
CUSTOMsingleCups.append(CUSTOMsingleForestCup)

CUSTOMsingleRainbowCup = {
	"Name": 'Rainbow Cup',
	"Track 1": 'Special Cup: Rainbow Road (MK8D)',
	"Track 2": 'Lightning Cup: Rainbow Road (N64)',
	"Track 3": 'Triforce Cup: Rainbow Road (SNES)',
	"Track 4": 'Moon Cup: Rainbow Road (3DS)'
}
CUSTOMsingleCups.append(CUSTOMsingleRainbowCup)

def randomiser():
	# variable setup
	x = 0
	duplicates = []

	# logic
	print("Mario Kart 8 Deluxe Randomiser")
	players = int(input("Enter the number of players [1-4] >  "))
	customCupQuery = input("Would you like to use one of our custom cups? [Y, N] > ").upper()
	if customCupQuery == 'N': numOfTracks = int(input("Enter the number of tracks you are playing [4, 6, 8, 12, 16, 24, 32, 48] > "))
	while x != players:
		x += 1
		characterRoll = choice(character)
		kartRoll = choice(kart)
		wheelRoll = choice(wheels)
		gliderRoll = choice(glider)
		print(f"\nPlayer {x}\n--Character: {characterRoll}\n--Kart: {kartRoll}\n--Wheels: {wheelRoll}\n--Glider: {gliderRoll}\n")
	if customCupQuery == 'N':
		print("Press enter to continue to the tracks, and then again to reveal the next track: ") # had to add the if statement so that it would only show up now cause it wouldn't make sense otherwise
		input()
	if customCupQuery == 'N':
		print('\n' * 1000)
		for x in range(numOfTracks):
			trackRoll = choice(track)
			if trackRoll in duplicates: trackRoll = choice(track) # removes duplicates by checking if they have already been added to the array, and then rerolling if it has
			duplicates.append(trackRoll)
			print(f"\nTrack {x+1}\n{trackRoll}")
			if x+1 != numOfTracks: input()
	elif customCupQuery == 'Y':
		cupLengthQuery = input("Enter the length of cup you would like to play [[S]ingle (4), [D]ouble (8)]: ").upper()
		if cupLengthQuery == 'S':
			print("Enter the number corresponding to one of the following cups > ")
			for i in range(len(CUSTOMsingleCups)): print(f"\t{i+1}. {CUSTOMsingleCups[i]['Name']}")
			cupChoice = int(input("> "))
			print('\n'*1000 + f"THE {CUSTOMsingleCups[cupChoice-1]['Name'].upper()}")
			for i in range(len(CUSTOMsingleCups[0])-1): input(f"\nTrack {i+1}\n{CUSTOMsingleCups[cupChoice-1][f'Track {i+1}']}")
		if cupLengthQuery == 'D':
			print("We only have one double cup currently:")
			print('\n' * 1000 + "THE FOOD DOUBLE CUP")
			for i in range(len(CUSTOMdoubleFoodCup)):
				input(f"\n\nTrack {i+1}: \n{CUSTOMdoubleFoodCup[i]}")

def statRetriever():
	statType = int(input("Would you like the stats of a:\n\t1. Kart\n\t2. Wheel\n\t3. Glider\n\t4. Character\nEnter your number here: "))
	if statType == 1:
		kartStatsCSV = pd.read_csv("kartStats.csv")
		kartName = input("Enter the name of the kart you wants stats for: ")
		speed = kartStatsCSV[kartStatsCSV['Name'] == kartName].iloc[0, 1]
		acceleration = kartStatsCSV[kartStatsCSV['Name'] == kartName].iloc[0, 2]
		weight = kartStatsCSV[kartStatsCSV['Name'] == kartName].iloc[0, 3]
		handling = kartStatsCSV[kartStatsCSV['Name'] == kartName].iloc[0, 4]
		grip = kartStatsCSV[kartStatsCSV['Name'] == kartName].iloc[0, 5]
		miniTurbo = kartStatsCSV[kartStatsCSV['Name'] == kartName].iloc[0, 6]
		total = kartStatsCSV[kartStatsCSV['Name'] == kartName].iloc[0, 7]
		print(f"\n{kartName}\n--Speed: {speed}\n--Acceleration: {acceleration}\n--Weight: {weight}\n--Handling: {handling}\n--Grip: {grip}\n--Mini-Turbo: {miniTurbo}\n--Total: {total}\n")
	elif statType == 2:
		wheelStatsCSV = pd.read_csv("wheelStats.csv")
		wheelName = input("Enter the name of the wheels you wants stats for: ")
		speed = wheelStatsCSV[wheelStatsCSV['Name'] == wheelName].iloc[0, 1]
		acceleration = wheelStatsCSV[wheelStatsCSV['Name'] == wheelName].iloc[0, 2]
		weight = wheelStatsCSV[wheelStatsCSV['Name'] == wheelName].iloc[0, 3]
		handling = wheelStatsCSV[wheelStatsCSV['Name'] == wheelName].iloc[0, 4]
		grip = wheelStatsCSV[wheelStatsCSV['Name'] == wheelName].iloc[0, 5]
		miniTurbo = wheelStatsCSV[wheelStatsCSV['Name'] == wheelName].iloc[0, 6]
		total = wheelStatsCSV[wheelStatsCSV['Name'] == wheelName].iloc[0, 7]
		print(f"\n{wheelName}\n--Speed: {speed}\n--Acceleration: {acceleration}\n--Weight: {weight}\n--Handling: {handling}\n--Grip: {grip}\n--Mini-Turbo: {miniTurbo}\n--Total: {total}\n")
	elif statType == 3:
		gliderStatsCSV = pd.read_csv("gliderStats.csv")
		gliderName = input("Enter the name of the glider you wants stats for: ")
		speed = gliderStatsCSV[gliderStatsCSV['Name'] == gliderName].iloc[0, 1]
		acceleration = gliderStatsCSV[gliderStatsCSV['Name'] == gliderName].iloc[0, 2]
		weight = gliderStatsCSV[gliderStatsCSV['Name'] == gliderName].iloc[0, 3]
		handling = gliderStatsCSV[gliderStatsCSV['Name'] == gliderName].iloc[0, 4]
		grip = gliderStatsCSV[gliderStatsCSV['Name'] == gliderName].iloc[0, 5]
		miniTurbo = gliderStatsCSV[gliderStatsCSV['Name'] == gliderName].iloc[0, 6]
		print(f"\n{gliderName}\n--Speed: {speed}\n--Acceleration: {acceleration}\n--Weight: {weight}\n--Handling: {handling}\n--Grip: {grip}\n--Mini-Turbo: {miniTurbo}\n")
	elif statType == 4:
		characterStatsCSV = pd.read_csv("characterStats.csv")
		characterName = input("Enter the name of the character you wants stats for: ")
		speed = characterStatsCSV[characterStatsCSV['Name'] == characterName].iloc[0, 1]
		acceleration = characterStatsCSV[characterStatsCSV['Name'] == characterName].iloc[0, 2]
		weight = characterStatsCSV[characterStatsCSV['Name'] == characterName].iloc[0, 3]
		handling = characterStatsCSV[characterStatsCSV['Name'] == characterName].iloc[0, 4]
		grip = characterStatsCSV[characterStatsCSV['Name'] == characterName].iloc[0, 5]
		miniTurbo = characterStatsCSV[characterStatsCSV['Name'] == characterName].iloc[0, 6]
		total = characterStatsCSV[characterStatsCSV['Name'] == characterName].iloc[0, 7]
		print(f"\n{characterName}\n--Speed: {speed}\n--Acceleration: {acceleration}\n--Weight: {weight}\n--Handling: {handling}\n--Grip: {grip}\n--Mini-Turbo: {miniTurbo}\n--Total: {total}\n")

def builder():
	remove_content = ["\'", "[", "]"]
	opts = int(input("What would you like to do?\n\t1. List all characters\n\t2. List all karts\n\t3. List all wheels\n\t4. List all gliders\n\t5. Start the builder\nEnter your number here: "))
	if opts == 1: print(character.strip('\''))
	elif opts == 2: print(repr(kart))
	#//characterForBuilder = input("Enter the name of the character that you are using in the build (case-sensitive): ")
	#//kartForBuilder = input("Enter the kart you would like to use for this build (case-sensitive): ")
	#//wheelsForBuilder = input("Enter the wheels you are using (case-sensitive): ")
	#//gliderForBuilder = input("Enter the glider you want to use (case-sensitive): ")



print("Mario Kart 8 Deluxe Toolkit")
tool = int(input("Which tool would you like to use?\n\t1. Randomiser\n\t2. Stat Viewer\n\t3. Builder\n>  "))
if tool == 1:
	randomiser()
elif tool == 2:
	statRetriever()
elif tool == 3:
	builder()


#TODO add error handling to the randomiser
#TODO this could include only allowing the given number of tracks, correcting the wrong type inputted for either input
#TODO or asking if they want to roll again
