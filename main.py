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
bot = commands.Bot(command_prefix='f!', intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f"successfully logged in as {bot.user}")
    await bot.change_presence(status=nextcord.Status.idle, activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="f!help | FaithClient!"))


# Detect Joining Members
@bot.event
async def on_member_join(member: nextcord.Member):
    embed = nextcord.Embed(title="Heyo there!", 
        description=f"👋 {member.mention} Welcome to the server!\n\nWe hope you have a great time in here :D", 
        color=color
    )
    embed.set_thumbnail(url=member.default_avatar)
    await member.guild.get_channel(welcome_channel_id).send(embed=embed)


# Basic Ping Command
@bot.command()
async def ping(ctx):
    embed = nextcord.Embed(
        color=color,
        title="Ping Pong! 🏓"
    )
    embed.add_field(name='Bot Latency!', value=f"Bot ping is **{round(bot.latency * 1000)}ms**", inline=True)
    embed.set_author(name=bot.user, icon_url=bot.user.avatar)
    embed.set_thumbnail(url=bot.user.avatar)
    embed.set_footer(text=f"Requested by {ctx.author}")
    embed.timestamp = datetime.datetime.now()
    await ctx.send(embed=embed)


## Hebiscuit - Will continue on my own soon, i hate it
# # Help Command
# @bot.command()
# async def help(ctx):
#     embed = nextcord.Embed(
#         color=color,
#     )
#     embed.add_field(name='Basic Commands', value="""Ping 
#     Usage: f!ping
#     """, inline=True)
#     embed.set_author(name=bot.user, icon_url=bot.user.avatar)
#     embed.set_thumbnail(url=ctx.author.avatar.url)
#     embed.timestamp = datetime.datetime.utcnow()
#     embed.set_footer(text=f"Requested by {ctx.author}")
#     await ctx.send(embed=embed)

@bot.command()
async def rules(ctx):
    embed = nextcord.Embed(
        title="Rules",
        color=0xFF0000,
        description="Please follow these rules to potentially avoid a warn, mute or ban."
    )
    embed.set_image("https://cdn.discordapp.com/attachments/995611552768086057/995926271542448218/faithbg_copy.png")
    embed.add_field(
        name="Be respectful to other users and their privacy.",
        value="You must make sure you create a safe environment for others.",
        inline=False
    )
    embed.add_field(
        name="Do not post any NSFW content.",
        value="NSFW is not tolerated at all. You will receive an immediate ban for this action.",
        inline=False
    )
    embed.add_field(
        name="Do not spam.",
        value="Pretty self-explanatory, right?",
        inline=False
    )
    embed.add_field(
        name=f"Keep bot commands in #{bot.get_channel(942179597112475687)}.",
        value="The bot commands channel is there for a reason. Use it.",
        inline=False
    )
    embed.add_field(
        name="English only.",
        value="Please use English when talking in the chatrooms, it makes moderating easier and makes it easier for "
              "other people to understand you (as they are more likely to already know English).",
        inline=False
    )
    embed.add_field(
        name="Swearing is allowed, but with exceptions.",
        value="Swearing is fine for general conversation, however, we will not tolerate any insults or ways of using "
              "swearing in a negative way.",
        inline=False
    )
    embed.add_field(
        name="Use common sense.",
        value="Just because there might not be a rule listed here, doesn't give you the right to carry out any "
              "actions that may cause others to feel unsafe, hurt the server etc.",
        inline=False
    )
    embed.set_footer(text="Please note that these rules may change anytime.")
    await ctx.send(embed=embed)

# devgocri - removed the below code as the cogs folder was not pushed to github
# because it was empty, didnt have cog files in em yet

# Initialize Cogs
#for filename in os.listdir("./cogs"):
#    if filename.endswith(".py"):
#        bot.load_extension(f"cogs.{filename[:-3]}")
#        print(f"Successfully loaded {filename}")

# Runs Bot
if __name__ == "__main__":
    load_dotenv()
    bot.run(os.getenv("DISCORD_TOKEN"))
