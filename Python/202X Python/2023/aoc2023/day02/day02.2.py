totalPower = 0
with open("day02input.txt", 'r') as f:
	lines = f.readlines()

	# one loop is one game
	for line in lines:
		topGreen = 0
		topRed = 0
		topBlue = 0
		# remove the game id and any unneeded leading characters
		index = line.find(':') + 2
		noID = line[index:]

		# split each game pull into an array
		splitPulls = noID.split(';')

		# one loop is one pull
		for pull in splitPulls:
			noNewline = pull.replace('\n', '')
			noLeadingWhitespace = noNewline.lstrip()
			splitColours = noLeadingWhitespace.split(',')

			# one loop is one colour of cube from the pull
			for colour in splitColours:
				colour = colour.lstrip()

				if 'green' in colour:
					num = int(colour.replace(' green', ''))
					if num > topGreen:
						topGreen = num
					else:
						topGreen = topGreen

				elif 'red' in colour:
					num = int(colour.replace(' red', ''))
					if num > topRed:
						topRed = num
					else:
						topRed = topRed

				elif 'blue' in colour:
					num = int(colour.replace(' blue', ''))
					if num > topBlue:
						topBlue = num
					else:
						topBlue = topBlue

		power = topGreen * topBlue * topRed
		totalPower += power

print(totalPower)

