# Imports
import nextcord, os
import datetime

from nextcord.ext import commands
from nextcord.ext.commands import Context
from dotenv import load_dotenv

# Variables
welcome_channel_id = 942179597112475681
year = datetime.date.today().year
intents = nextcord.Intents.all()
color = 0xffd500

# Bot Initialization
bot = commands.Bot(command_prefix='f!', intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f"successfully logged in as {bot.user}")
    await bot.change_presence(status=nextcord.Status.idle, activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="f!help | FaithClient!"))


# Basic Ping Command
@bot.command(aliases=['latency', 'Ping', 'Latency'])
async def ping(ctx: Context):
    embed = nextcord.Embed(
        color=color,
        title="Ping Pong! 🏓"
    )
    embed.add_field(name='Bot Latency!', value=f"Bot ping is **{round(bot.latency * 1000)}ms**", inline=True)
    embed.set_author(name=bot.user, icon_url=bot.user.avatar)
    embed.set_thumbnail(url=bot.user.avatar)
    embed.set_footer(text=f"Requested by {ctx.author}")
    embed.timestamp = datetime.datetime.now()
    await ctx.reply(embed=embed)

# Initialize Cogs
for filename in os.listdir("./cogs"):
   if filename.endswith(".py"):
       bot.load_extension(f"cogs.{filename[:-3]}")
       print(f"Successfully loaded {filename}")


## To solve cog bugs if they occur
@bot.command()
async def load(ctx: Context):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
    await ctx.send("Loaded Cog!")

@bot.command()
async def unload(ctx: Context):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.unload_extension(f"cogs.{filename[:-3]}")
    await ctx.send("Unloaded Cog!")

@bot.command()
async def reload(ctx):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.reload_extension(f"cogs.{filename[:-3]}")
    await ctx.send("Reloaded Cog!")

# Runs Bot
if __name__ == "__main__":
    load_dotenv()
    bot.run(os.getenv("DISCORD_TOKEN"))
