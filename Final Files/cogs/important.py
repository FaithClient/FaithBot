import nextcord, asyncio, datetime

from nextcord.ext import commands
from nextcord.ext.commands import Context

class Important(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx: Context, error: Exception):
        embed = nextcord.Embed(title="An exception was raised", description=f"Details: {error}", color=nextcord.Color.dark_red())
        await ctx.send(embed=embed)
    
    @commands.command()
    # @commands.has_role("Owner")
    async def download(self, ctx: Context, title: str = None, ver: str = None, link = None, *, description: str):
        await ctx.message.delete()
        if title == None or ver == None or link == None:
            msg = await ctx.send(f"{ctx.author.mention} You need to specify a title / version / link")
            await asyncio.sleep(5)
            await msg.delete()
            return
        pictures = [p.url for p in ctx.message.attachments]
        embed = nextcord.Embed(title=f"{title} {ver}", description=f"{description}\nDownload Link: {link}", color=nextcord.Color.brand_green())
        embed.set_thumbnail(url=self.bot.user.avatar)
        #embed.set_image()
        embed.set_footer(text=f"Announced by {ctx.author}")
        embed.timestamp = datetime.datetime.now()
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("▶")

def setup(bot: commands.Bot):
    bot.add_cog(Important(bot))