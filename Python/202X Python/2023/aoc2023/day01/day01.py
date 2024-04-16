import string

lowerLetters = list(string.ascii_lowercase)
numbersAsWords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
runningTotal = 0

with open("day01input.txt", "r") as f:
    line = f.readlines()
    print(line)
    for i in line:
        # remove newline characters
        noNewline = i.replace("\n", "")
        noWords = noNewline

        # check for numbers as words here
        for i in numbersAsWords:
            numWordSplitToArray = [*i]
            numInMiddle = numWordSplitToArray[0] + str(numbersAsWords.index(i) + 1) + numWordSplitToArray[len(i) - 1]
            noWords = noWords.replace(i, numInMiddle)

        # removes all other letters here
        noLetters = noWords
        for i in lowerLetters:
            noLetters = noLetters.replace(i, "")

        # checks if number is a single digit long, in which case, concatenate itself to it
        doubledSingleNum = noLetters
        if len(doubledSingleNum) == 1:
            doubledSingleNum = noLetters + noLetters
        elif len(doubledSingleNum) > 1:
            doubledSingleNum = doubledSingleNum

        # splits the number into characters in an array
        iSplit = [*doubledSingleNum]

        # takes the first [0] and last [len(x)-1] characters of the array and concatenates
        lineNumber = iSplit[0] + iSplit[len(iSplit)-1]
        # adds the 2-digit number to the running total variable
        runningTotal += int(lineNumber)

print(runningTotal)
