import nextcord, asyncio, datetime

from nextcord.ext import commands
from nextcord.ext.commands import Context

class Suggesting(commands.Cog, name="Suggestions"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.s_ch_id = 942179597112475685
    
    @commands.command()
    async def suggest(self, ctx: Context, *, suggestion: str = None):
        await ctx.message.delete()
        if suggestion == None:
            msg = await ctx.send(f"{ctx.author.mention} You need to add a suggestion!!")
            await asyncio.sleep(3)
            await msg.delete()
            return
        suggestion_channel = ctx.guild.get_channel(self.s_ch_id)
        embed = nextcord.Embed(
            description=suggestion,
            color = nextcord.Color.green()
        )
        embed.set_author(
            name = f"{ctx.author.name}'s suggestion",
            icon_url = ctx.author.avatar if ctx.author.avatar is not None else ctx.author.default_avatar
        )
        embed.set_thumbnail(
            url = self.bot.user.avatar
        )
        embed.timestamp = datetime.datetime.now()
        # msg = await suggestion_channel.send(embed=embed)
        msg = await suggestion_channel.send(embed=embed)
        await msg.add_reaction("⬆")
        await msg.add_reaction("⬇")
        ans = await ctx.send(f"{ctx.author.mention} Your suggestion was successfully forwarded to {ctx.guild.get_channel(self.s_ch_id).mention}")
        await asyncio.sleep(6)
        await ans.delete()

def setup(bot: commands.Bot):
    bot.add_cog(Suggesting(bot))