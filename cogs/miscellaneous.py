from ast import alias
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

class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @bot.command(aliases=['Avatar', 'av', 'Av'])
    async def avatar(self, ctx, *, member: nextcord.Member = None):
        if member == None:
            member = ctx.author
        embed = nextcord.Embed(title=f"{member.name}'s Avatar", color=color)
        embed.set_image(url=member.avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.timestamp = datetime.datetime.now()
        await ctx.reply(embed=embed)
    
    @bot.command(aliases=['Sexo'])
    async def sexo(self, ctx):
        embed = nextcord.Embed(title="Sexo", color=color, description="- Bedezu")
        embed.set_footer(text=f"Requested by {ctx.author} | 😳")
        embed.set_image(url='https://cdn.shopify.com/s/files/1/1061/1924/products/Flushed_Emoji_Icon_5e6ce936-4add-472b-96ba-9082998adcf7_grande.png')
        embed.timestamp = datetime.datetime.now()
        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(Miscellaneous(bot))