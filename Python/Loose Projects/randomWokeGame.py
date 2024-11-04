import requests
import pandas as pd
import os
import random

# Define the URL and file path
url = "https://wokedetector.cirnoslab.me/data.csv"
file_path = os.path.join(os.path.dirname(__file__), 'wokeData.csv')

# Download the CSV file and save it
response = requests.get(url)
with open(file_path, 'wb') as file:
    file.write(response.content)

# Load the CSV data into a DataFrame
woke_data = pd.read_csv(file_path)

# Get the number of rows
num_rows = len(woke_data)

# Select a random game name
random_index = random.randint(0, num_rows - 1)  # Adjusted to avoid IndexError
game_name = woke_data.iloc[random_index, 1]

print(game_name)



# TO USE: https://www.datacamp.com/tutorial/fuzzy-string-python