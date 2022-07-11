<<<<<<< HEAD
import nextcord, datetime
=======
from ast import alias
from discord import Embed
import nextcord
>>>>>>> f16eb23b3086000e320c1d7ca28453f405befe77
from nextcord.ext import commands
from nextcord.ext.commands import Context

year = datetime.date.today().year
color = 0xffd500

class Miscellaneous(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
<<<<<<< HEAD
    @commands.command(aliases=['Avatar', 'Av', 'av'])
    async def avatar(self, ctx: Context, *, member: nextcord.Member = None):
=======
    @bot.command(aliases=['Avatar', 'av', 'Av'])
    async def avatar(self, ctx, *, member: nextcord.Member = None):
>>>>>>> f16eb23b3086000e320c1d7ca28453f405befe77
        if member == None:
            member = ctx.author
        embed = nextcord.Embed(title=f"{member.name}'s Avatar", color=color)
        embed.set_image(url=member.avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.timestamp = datetime.datetime.now()
<<<<<<< HEAD
        await ctx.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        embed = nextcord.Embed(title="Sexo", color=color, description="- Bedezu")
        embed.set_footer(text=f"Requested by {message.author} | 😳")
        embed.set_image(url='https://cdn.shopify.com/s/files/1/1061/1924/products/Flushed_Emoji_Icon_5e6ce936-4add-472b-96ba-9082998adcf7_grande.png')
        embed.timestamp = datetime.datetime.now()
        if message.content.startswith("sexo") or message.content.startswith("Sexo"):
            await message.reply(embed=embed) 
=======
        await ctx.reply(embed=embed)
    
    @bot.command(aliases=['Sexo'])
    async def sexo(self, ctx):
        embed = nextcord.Embed(title="Sexo", color=color, description="- Bedezu")
        embed.set_footer(text=f"Requested by {ctx.author} | 😳")
        embed.set_image(url='https://cdn.shopify.com/s/files/1/1061/1924/products/Flushed_Emoji_Icon_5e6ce936-4add-472b-96ba-9082998adcf7_grande.png')
        embed.timestamp = datetime.datetime.now()
        await ctx.reply(embed=embed)
>>>>>>> f16eb23b3086000e320c1d7ca28453f405befe77

def setup(bot: commands.Bot):
    bot.add_cog(Miscellaneous(bot))