# Text Based Prison Escape Game
# Made by traditionallimb (tradlimb)
# Started May 2020
# Finished ___ ___

from time import sleep as slp
from random import choice as chce
from random import randint as rand
import pyfiglet

cyan = "\033[1;36m"
red = "\033[1;33m"
green = "\033[1;32m"

import sys
def scrollTxt(text):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    slp(0.03)

roommate = None
crimes = ["Murder", "Arson", "Drug Abuse", "Domestic Abuse"]
crime = chce(crimes)
age = rand(14, 25)
def roommatePicker(file_name):
  """Choose a line at random from the text file"""
  with open(file_name, 'r') as file:
    lines = file.readlines()
    global roommate
    roommate = chce(lines)
    roommate = roommate.strip('\n')




def intro():
  intro = cyan + "Hello. Today, you were arrested and you plan to escape this prison compound. But first, the guards want to know your name." + green + "\nWhat is it? " + cyan

  scrollTxt(intro)
  name = str(input())

  if name in open("boyNames").read():
    gender = "Male"
    roommatePicker("boyNames")
  elif name in open("girlNames").read():
    gender = "Female"
    roommatePicker("girlNames")
  else:
    scrollTxt(cyan + "What is your gender? " + green + "[Male]" + cyan + " or " + green +"[Female] " + cyan)
    ans = str(input()).lower()
    if ans == 'male':
      f = open("boyNames", "a")
      f.write(name + "\n")
      f.close()
      roommatePicker("boyNames")
      gender = "Male"
    elif ans == 'female':
      f = open("girlNames", "a")
      f.write(name + "\n")
      f.close()
      roommatePicker("girlNames")
      gender = "Female"


  intro2 = cyan + "The guards come up to you, and say, \"Hello " + red + name + cyan + ". You have been arrested for " + red + crime + cyan + ". The " + red + gender + cyan + " dorms are over there. Make sure you go to the " + red + str(age) + cyan + " year old section, and roll call will be at 9:30.\"\n"

  scrollTxt(intro2)

def dayOne():
  scrollTxt("Your are woken up at 07:30 by the guards going around banging on the cell doors. Your roommate " + red + roommate + cyan + ", groans as they pull themselves out of their bed. They turn to you, and say \"How about we bust out, you know prison-escape movie style?\"" + green + "[Yes]" + cyan + "or" + green + "[No]")
  ans = str(input()).lower()
  if ans == 'yes':



intro()
slp(0.5)
print(pyfiglet.figlet_format("Day One"))
slp(0.5)
dayOne()

slp(2)
