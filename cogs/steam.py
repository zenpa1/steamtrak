# -- STEAM-RELATED COMMANDS --
from discord.ext import bridge, commands
from utils.steam_api import get_steam_profile_data, resolve_vanity_url, get_steam_game_data
from utils.embeds import build_profile_embed

class Steam(commands.Cog):
    def __init__(self, bot):  # Called when cog is loaded
        self.bot = bot
    
    # Fetch steam data
    @bridge.bridge_command(name="fetch", description="Fetch Steam data.")
    async def fetch(self, ctx, profile_identifier):
        try:
            # Check if input is a SteamID, else resolve custom URL
            if profile_identifier.isdigit() and len(profile_identifier) == 17:
                steam_id = profile_identifier
            else:
                steam_id = resolve_vanity_url(profile_identifier)
            if steam_id:
                print("✨ Successfully taken Steam ID!")

            # Get Steam profile through Steam ID
            profile_data = get_steam_profile_data(steam_id)
            if profile_data:
                print("✨ Successfully taken Steam profile!")

            # Get Steam profile game data through Steam ID
            game_data = get_steam_game_data(steam_id)
            if game_data:
                print("✨ Successfully taken game data!")

            # Create embed
            embed_msg = build_profile_embed(profile_data, game_data)
            if embed_msg:
                print("✨ Successfully built embed!")

            await ctx.respond(embed=embed_msg)

        except Exception as e:
            error_msg = f"🔴 Error with fetch command: {str(e)}"
            print(error_msg)
            await ctx.respond(error_msg)

def setup(bot):  # Setup cog
    bot.add_cog(Steam(bot))  # Add cog to bot