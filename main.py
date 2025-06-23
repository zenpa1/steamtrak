# -- BOT ENTRY POINT --
import discord
from discord.ext import bridge, commands
from dotenv import load_dotenv
import json
import os

# Load .env (secrets)
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")  # Loads Discord token from .env

# Load configuration
with open('config.json') as f:
    config = json.load(f)

# Privileged Gateway Intents
intents = discord.Intents().all()

# Set prefix and intents (bridge for both prefix/slash commands)
bot = bridge.Bot(command_prefix=commands.when_mentioned_or(config['prefix']), intents=intents, heartbeat_timeout=120)

# Load cogs on startup
def load_cogs():
    cogs_list = [
        "steam"
    ]

    for cog in cogs_list:
        bot.load_extension(f'cogs.{cog}')

@bot.event
async def on_ready():
    print(f"🔵 {bot.user} is ready to go!")
    await setup_hook()

async def setup_hook():
    try:
        load_cogs()
        game = discord.Game("on Steam! :3")
        await bot.change_presence(activity=game)
        try:
            await bot.sync_commands(guild_ids=config['guilds'])  # Sync slash commands
            print("🟢 Slash commands synced! (^ω^)")
        except Exception as e:
            print(f"🔴 Failed to sync! {str(e)}")
    except Exception as e:
        print(f"🔴 Failed to load cogs! {str(e)}")

bot.run(TOKEN)