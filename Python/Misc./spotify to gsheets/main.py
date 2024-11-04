import pygsheets
import os
import json
import csv
import spotipy
import pandas as pd
from google.oauth2 import service_account
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv, dotenv_values

load_dotenv()


# google auth
with open('credentials.json') as source:
    info = json.load(source)
credentials = service_account.Credentials.from_service_account_info(info)
client = pygsheets.authorize(service_account_file='credentials.json')
spreadsheetURL = "https://docs.google.com/spreadsheets/d/1OagFBoa3Qo33W8cnYLtSWOfUqMiWe9tyDmF7ySR5s3k/edit?usp=sharing"
sheet_data = client.sheet.get("1OagFBoa3Qo33W8cnYLtSWOfUqMiWe9tyDmF7ySR5s3k")

sheet = client.open_by_key("1OagFBoa3Qo33W8cnYLtSWOfUqMiWe9tyDmF7ySR5s3k")
wks = sheet.worksheet_by_title("music i have listened to")

# print(wks.get_all_values())


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET")))

user = sp.user('traditionallimb')
print(user)