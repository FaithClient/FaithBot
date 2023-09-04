import discord, datetime, humanfriendly
from discord.ext import commands
from discord.ext.commands import Context

year = datetime.date.today().year
color = 0xffd500

class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


def setup(bot: commands.Bot):
    bot.add_cog(Moderation(bot))
