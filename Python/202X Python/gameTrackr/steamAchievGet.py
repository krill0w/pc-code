import requests

url = "http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=440&key=406499F72B871BA02972C93877D5B744&steamid=76561198436661503"
steamKey = "406499F72B871BA02972C93877D5B744"

response = requests.request("GET", url, params="apiname")

print(response.text)