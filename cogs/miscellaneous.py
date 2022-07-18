import nextcord, datetime
from nextcord.ext import commands
from nextcord.ext.commands import Context

year = datetime.date.today().year
color = 0xffd500

class Miscellaneous(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(aliases=['latency', 'Ping', 'Latency'])
    async def ping(self, ctx: Context):
        embed = nextcord.Embed(
            color=color,
            title="Ping Pong! 🏓"
        )
        embed.add_field(name='Bot Latency!', value=f"Bot ping is **{round(self.bot.latency * 1000)}ms**", inline=True)
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar)
        embed.set_thumbnail(url=self.bot.user.avatar)
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.timestamp = datetime.datetime.now()
        await ctx.reply(embed=embed)
    
    @commands.command(aliases=['Avatar', 'Av', 'av', 'AVATAR', 'AV', 'PFP', 'pfp', 'Pfp'])
    async def avatar(self, ctx: Context, *, member: nextcord.Member = None):
        if member == None:
            member = ctx.author
        memberAv = member.avatar.url

        embed = nextcord.Embed(title=f"{member.name}'s Avatar", color=color)
        embed.set_image(url=memberAv)
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)
    
    @commands.command(aliases=['serverinfo', 'server'])
    async def serverstats(self, ctx: Context):
        embed = nextcord.Embed(title='Server Stats ↗', color=color)
        await ctx.send(f"These are the current server stats ↗ {ctx.author.mention}!", embed=embed)


    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        embed = nextcord.Embed(color=color, description="‎\n**Sexo**\n- Bedezu")
        embed.set_footer(text=f"Requested by {message.author} | 😳")
        embed.set_thumbnail(url='https://cdn.shopify.com/s/files/1/1061/1924/products/Flushed_Emoji_Icon_5e6ce936-4add-472b-96ba-9082998adcf7_grande.png')
        embed.timestamp = datetime.datetime.now()
        if message.content.startswith("sexo") or message.content.startswith("Sexo"):
            await message.reply(embed=embed) 

def setup(bot: commands.Bot):
    bot.add_cog(Miscellaneous(bot))
