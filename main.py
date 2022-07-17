# Imports
import nextcord, os, datetime, asyncio

from cogs import important
from nextcord.ext import commands
from nextcord.ext.commands import Context
from dotenv import load_dotenv

# Variables
welcome_channel_id = 942179597112475681
year = datetime.date.today().year
intents = nextcord.Intents.all()
color = 0xffd500

# Bot Initialization
bot = commands.Bot(command_prefix='ft!', intents=intents)

@bot.event
async def on_ready():
    print(f"successfully logged in as {bot.user}")
    await bot.change_presence(status=nextcord.Status.idle, activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="f!help | FaithClient!"))
    
# Initialize Cogs
for filename in os.listdir("./cogs"):
   if filename.endswith(".py") and filename != "__init__.py":
       bot.load_extension(f"cogs.{filename[:-3]}")
       print(f"Successfully loaded {filename}")


## To solve cog bugs if they occur
@bot.command()
async def load(ctx: Context):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            bot.load_extension(f"cogs.{filename[:-3]}")
    await ctx.send("Loaded Cogs!")

@bot.command()
async def unload(ctx: Context):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            bot.unload_extension(f"cogs.{filename[:-3]}")
    await ctx.send("Unloaded Cogs!")

@bot.command()
async def reload(ctx: Context):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            bot.reload_extension(f"cogs.{filename[:-3]}")
    await ctx.send("Reloaded Cogs!")

# Runs Bot
if __name__ == "__main__":
    load_dotenv()
    bot.run(os.getenv("DISCORD_TOKEN"))
