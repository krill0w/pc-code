from steamwebapi import profiles
from decouple import config

KEY = config("STEAM_API_KEY")
user_profile = profiles.get_user_profile("traditionallimb")
print(vars(user_profile))