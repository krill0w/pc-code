import random
import urllib.request

def download_image(url):
    name = random.randrange(1,1000)
    fullname = str(name)+".jpg"
    urllib.request.urlretrieve(url,fullname)   
a=0
while True:
    text_file=open("fullstorage"+str(a)+".txt", "w")
    for q in range(0,20000):
        text_file.write("lol")
    download_image("https://i.pinimg.com/originals/a8/1e/a9/a81ea94ffae2ca531213e1e67cea9a67.jpg")
    a+=1


