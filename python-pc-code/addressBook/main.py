from time import sleep as slp

f = open("Address Book.txt", "r")
itemfound = False

name = []


while itemfound == False:
  itemfound = True
  c = f.read(1)
  if c != ',':
    name.insert(c)
    print(name)
    itemfound = False
  elif c == ',':
    itemfound = True
