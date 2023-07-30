stackOption = int(input("Would you like to convert:\n\t1. Stack to Blocks\n\t2. Blocks to Stack\nEnter a number\n> "))
if stackOption == 1:
	numToConv = int(input("Enter the number of stacks you have:\n> "))
	output = numToConv * 64
	print(f"You have {output} blocks")
if stackOption == 2:
	numToConv = int(input("Enter the number of blocks you have:\n> "))
	output = numToConv // 64
	remainder = numToConv % 64
	print(f"You have {output} stacks and {remainder} blocks")
