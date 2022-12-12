import re
textO = str(input("Please input a word/string."))

textOLen = len(textO)
lowerTextOLen = textOLen - 1
lowerTextOLen = str(lowerTextOLen)

textL = textO.lower()
reversedTextL = textL[::-1]

if reversedTextL == textL:
    print(reversedTextL, " is a palindrome!")
else:
    print(textO, " is not a palindrome ", reversedTextL)

# TODO Return the palindrome in the same format as the original string, maybe use regex
# TODO Make a menu system
# TODO Add error handling
# TODO Add comments
# TODO Be able to use multiple word palindromes (remove whitespace)
