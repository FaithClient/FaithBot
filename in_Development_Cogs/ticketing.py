import discord, datetime
from discord import ApplicationContext as Context
from discord import Option
from discord.ext import commands

year = datetime.date.today().year
color = 0xffd500

class Ticketing(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    
def setup(bot: commands.Bot):
    bot.add_cog(Ticketing(bot))