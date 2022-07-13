import nextcord, datetime

from nextcord.ext import commands
from nextcord.ext.commands import Context

year = datetime.date.today().year
color = 0xffd500

class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def test(self, ctx):
        ctx.reply("moderation cog works!")

def setup(bot: commands.Bot):
    bot.add_cog(Moderation(bot))