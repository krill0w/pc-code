import requests
import json

parameters = {
  'name': 'Chandra'
}

response = requests.get('https://api.magicthegathering.io/v1/cards', params=parameters)


def jprint(obj):
  text = json.dumps(obj, sort_keys=True, indent=4)
  print(text)


print(response.status_code)
jprint(response.json())