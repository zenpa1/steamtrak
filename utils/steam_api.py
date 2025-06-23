# -- STEAM DATA FETCHER --
import os
import requests

STEAM_KEY = os.getenv("STEAM_API_KEY")

def get_steam_profile_data(steam_id):
    # Make an API call to v0002 (default profile getter)
    url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={STEAM_KEY}&steamids={steam_id}"
    data = requests.get(url)
    if data.status_code == 200:  # If GET was successful
        print("✨ Fetched Steam profile! (v0002)")
    return data.json()  # Return JSON

def resolve_vanity_url(vanity_name):
    # Make an API call to v1 (resolves vanity names)
    url = f"https://api.steampowered.com/ISteamUser/ResolveVanityURL/v1/?key={STEAM_KEY}&vanityurl={vanity_name}"
    data = requests.get(url)
    if data.status_code == 200:  # If GET was successful
        print("✨ Resolved vanity name! (v1)")
    parsed_data = data.json()
    return parsed_data['response']['steamid']  # Return SteamID

def get_steam_game_data(steam_id):
    # Make an API call to v0001 (get top 3 games)
    url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={STEAM_KEY}&steamid={steam_id}&include_appinfo=1&include_played_free_games=1"
    data = requests.get(url)
    if data.status_code == 200:  # If GET was successful
        print("✨ Fetched game data! (v0001)")
    return data.json()  # Return JSON