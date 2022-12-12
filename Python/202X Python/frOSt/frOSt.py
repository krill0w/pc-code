#frOSt; a dumb project where i try to make something similar to a terminal
#by traditionallimb
#started 29/12/2020
#finished __/__/____





"""  *[SETUP]*  """


"""  [MODULES]  """
from random import randint as ra
from time import sleep as s


"""  [VARIABLES]  """
loadTime = ra(2, 10)
loop = 1
currentDir = 'C:\\'


"""  [BOOTING]  """
print('frOSt 0.1P\n')
print('Booting into initial Alpha Build....')
s(loadTime)
print('\n\n\nfrOSt 0.1P')


"""  *[MAIN LOOP]*  """
while loop == 1:
  loop = 2

  command = input(currentDir + '>')

  if command == 'help':
    print("hello {name} | Says hello to you (how exciting)\n")
    loop = 1
  elif command == 'hello':
    print('Hello!\n')
    loop = 1
  elif command == 'exit' or command == 'shutdown':
    print('Shutting Down....\n')
    s(2)
    loop = 3
  else:
    print("Sorry, that command doesn't exist\n")
    loop = 1