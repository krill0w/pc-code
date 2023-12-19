import string

lowerLetters = list(string.ascii_uppercase)
runningTotal = int(0)
formattedList = []

with open("day01input.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    for i in lines:
        toString = lines[1]
        lineAsStr = str(toString)
        noLetters = lineAsStr.strip(lowerLetters)
        noLetters = noLetters.strip("/")
        formattedList.append(noLetters)

    for line in noLetters:
        singleNumbers = [int(num) for num in str(line)]
        lineAns = sum(singleNumbers)
        runningTotal += lineAns

print(runningTotal)