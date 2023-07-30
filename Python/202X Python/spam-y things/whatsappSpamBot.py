import pyautogui, time
time.sleep(5)
f= open('e:/Creativeness Productions/Coding/2020 Python/spam-y things/beemovie.txt', 'r')
for line in f:
  pyautogui.typewrite(line)
  pyautogui.press("enter")
  time.sleep(.5)