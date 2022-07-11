# Imports
import nextcord, os
import datetime
from nextcord.ext import commands
from dotenv import load_dotenv

# Variables
welcome_channel_id = 942179597112475681
year = datetime.date.today().year
intents = nextcord.Intents.all() 
intents.members = True
color = 0xffd500

# Bot Initialization
bot = commands.Bot(command_prefix='f!', intents=intents)


# Bot On Ready
@bot.event
async def on_ready():
    print(f"successfully logged in as {bot.user}")
    await bot.change_presence(status=nextcord.Status.idle, activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="f!help | FaithClient!"))

# Detect Joining Members
@bot.event
async def on_member_join(member: nextcord.Member):
    embed = nextcord.Embed(title="Heyo there!", description=f"👋 {member.mention} Welcome to the server!\n\nWe hope you have a great time in here :D", color=color)
    embed.set_thumbnail(url=member.default_avatar)
    await member.guild.get_channel(welcome_channel_id).send(embed=embed)


# Basic Ping Command
@bot.command()
async def ping(interaction):
    embed = nextcord.Embed(
        color=color,
        title="Ping Pong! 🏓",
    )
    embed.add_field(name='Bot Latency!', value=f"Bot ping is **{round(bot.latency * 1000)}ms**", inline=True)
    embed.set_author(name=bot.user, icon_url=bot.user.avatar)
    embed.set_thumbnail(url=bot.user.avatar)
    embed.set_footer(text=f"Requested by {interaction.message.author}")
    embed.timestamp = datetime.datetime.utcnow()
    await interaction.send(embed=embed)

# Initialize Cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"Successfully loaded {filename}")

# Runs Bot
if __name__ == "__main__":
    load_dotenv()
    bot.run(os.getenv("DISCORD_TOKEN"))