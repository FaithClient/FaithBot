import nextcord, datetime
from nextcord.ext import commands
from nextcord.ext.commands import Context

year = datetime.date.today().year
color = 0xffd500

class Miscellaneous(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
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


def setup(bot: commands.Bot):
    bot.add_cog(Miscellaneous(bot))
