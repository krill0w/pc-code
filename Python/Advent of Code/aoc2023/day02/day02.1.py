runningTotal = 0
with open("day02input.txt", 'r') as f:
	lines = f.readlines()

	for line in lines:
		excessive = False
		# remove the game id and any unneeded leading characters
		index = line.find(':') + 2
		noID = line[index:]

		# split each game pull into an array
		splitPulls = noID.split(';')

		for pull in splitPulls:
			noNewline = pull.replace('\n', '')
			noLeadingWhitespace = noNewline.lstrip()
			splitColours = noLeadingWhitespace.split(',')
			for colour in splitColours:
				colour = colour.lstrip()
				if 'green' in colour:
					num = int(colour.replace(' green', ''))
					if num > 13:
						excessive = True
					else:
						pass
				elif 'red' in colour:
					num = int(colour.replace(' red', ''))
					if num > 12:
						excessive = True
					else:
						pass
				elif 'blue' in colour:
					num = int(colour.replace(' blue', ''))
					if num > 14:
						excessive = True
					else:
						pass
		if excessive == True:
			print("not possible")
		elif excessive == False:
			idNum = line[:index].replace('Game ', '')
			idNumNoColon = int(idNum.replace(':', ''))
			runningTotal += idNumNoColon
			print(runningTotal)

