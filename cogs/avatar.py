from discord import Embed
import nextcord
from nextcord.ext import commands
import datetime

year = datetime.date.today().year
intents = nextcord.Intents.all()
intents.members = True
color = 0xffd500

# Bot Initialization
bot = commands.Bot(command_prefix='f!', intents=intents)

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @bot.command()
    async def avatar(self, ctx, *, member: nextcord.Member = None):
        if member == None:
            member = ctx.author
        memberAv = member.avatar.url
        embed = nextcord.Embed(title=f"{member.name}'s Avatar", color=color)
        embed.set_image(url=memberAv)
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Avatar(bot))