import pyautogui, time
time.sleep(5)
f= open('D:\Coding\pc-code\Python\\202X Python\spam-y things\\beemovie.txt', 'r')
for line in f:
  pyautogui.typewrite(line)
  pyautogui.press("enter")
  time.sleep(.5)