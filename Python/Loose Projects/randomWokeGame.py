import requests
import pandas as pd
import os


url = ("https://wokedetector.cirnoslab.me/data.csv")
my_local_file = os.path.join(os.path.dirname(__file__), 'some_file.txt')

myfile = requests.get(url)
open('/home/dom/Documents/pc-code/Python/202X Python/2024/wokeData.csv', 'wb').write(myfile.content)
print(os.path)

wokeDataCSV = pd.read_csv("wokeData.csv")