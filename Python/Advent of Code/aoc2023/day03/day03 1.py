allLines = []
symbolList = ['@', '$', '%', '&', '*', '-', '=', '+', '/']
currentLineSplit = []
nextLineSplit = []
numberIndexes = []
discard = []
result = ""
temp = ""

with open("day03 input.txt", "r") as f:
  line = f.readlines()
  for i in line:
    # remove newline characters
    noNewline = i.replace("\n", "")
    allLines.append(noNewline)

  for x in range(len(allLines)):

    # handle first line to prevent wrapping
    if x == 0:
      currentLine = allLines[x]
      nextLine = allLines[x+1]

      # split every character into own item in array
      for char in currentLine:
        currentLineSplit.append(char)
      for char in nextLine:
        nextLineSplit.append(char)

      # create an array of the index of every number
      for index, value in enumerate(currentLineSplit):
        if value.isdigit():
          numberIndexes.append(index)
      print(numberIndexes)

      for index in numberIndexes:
        if nextLineSplit[index-1] in symbolList or nextLineSplit[index+1] in symbolList or nextLineSplit[index] in symbolList:
          print(index, "next to symbol")


      
      """
       for item in currentLineSplit:
        if item.isdigit():
          temp += item
        elif temp:
          result += temp + " "
          temp = ""
      if temp:
        result += temp

      print(result)
      """          
     
    
    # normal operating
    elif len(allLines)-1 > x > 0:
      previousLine = allLines[x-1]
      currentLine = allLines[x]
      nextLine = allLines[x+1]

    # handle last line to prevent error
    elif x == len(allLines):
      previousLine = allLines[x-1]
      currentLine = allLines[x]
