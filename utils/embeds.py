# -- EMBED CREATOR --
import discord
import math

def build_profile_embed(profile_data, game_data):
    try:
        # Profile data retrieved through JSON (dict > dict > list > dict)
        profile_name = return_steam_name(profile_data)
        profile_url = return_steam_url(profile_data)
        profile_avatar = return_steam_avatar(profile_data)
        profile_status = return_steam_status(profile_data)

        # Game data retrieved through JSON (dict > dict > list > dict)
        games = game_data['response']['games']
        total_games = game_data['response']['game_count']

        # Sort games by playtime_forever in descending order
        sorted_games = sorted(games, key=lambda x: x['playtime_forever'], reverse=True)

        # Select top 3 games
        top_3_games = sorted_games[:3]

        # Create embed
        embed = discord.Embed(
            title=f"{profile_name}",
            url=f"{profile_url}",
            color=discord.Colour.blurple(),
        )
        embed.add_field(name="Status", value=profile_status, inline=True)
        embed.add_field(name="Total Games", value=total_games, inline=True)
        embed.add_field(name=f"{top_3_games[0]['name']}", value=f"{math.floor(top_3_games[0]['playtime_forever'] / 60)} hours", inline=False)
        embed.add_field(name=f"{top_3_games[1]['name']}", value=f"{math.floor(top_3_games[1]['playtime_forever'] / 60)} hours", inline=False)
        embed.add_field(name=f"{top_3_games[2]['name']}", value=f"{math.floor(top_3_games[2]['playtime_forever'] / 60)} hours", inline=False)
        embed.set_thumbnail(url=profile_avatar)
        embed.set_footer(text="steamtrak developed by zenpa1", icon_url="https://avatars.steamstatic.com/c325fe9e3050bfb27f210bdbc9a46d68e193f797_full.jpg")

        return embed
    except Exception as e:
        print(f"❌ Error in build_profile_embed: {str(e)}")

def return_steam_name(data):
    name = data['response']['players'][0]['personaname']
    try:
        return name
    except Exception as e:
        print(f"❌ Error in return_steam_name: {str(e)}")

def return_steam_url(data):
    url = data['response']['players'][0]['profileurl']
    try:
        return url
    except Exception as e:
        print(f"❌ Error in return_steam_url: {str(e)}")

def return_steam_avatar(data):
    avatar = data['response']['players'][0]['avatarfull']
    try:
        return avatar
    except Exception as e:
        print(f"❌ Error in return_steam_avatar: {str(e)}")

def return_steam_status(data):
    status = data['response']['players'][0]['personastate']
    # Depending on status, return a value
    if status == 0:
        return "⚫ Offline"
    elif status == 1:
        return "🟢 Online"
    elif status == 2:
        return "🔴 Busy"
    elif status == 3:
        return "🔵 Away"
    elif status == 4:
        return "🟣 Snooze"
    elif status == 5:
        return "🟠 Looking to trade"
    elif status == 6:
        return "🟡 Looking to play"
    else:
        return "❓ Unknown Status"
    
