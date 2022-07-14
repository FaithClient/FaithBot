import nextcord, asyncio, datetime

from nextcord.ext import commands
from nextcord.ext.commands import Context

class Important(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.d_ch_id = 942179597112475678
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx: Context, error: Exception):
        embed = nextcord.Embed(title="An exception was raised", description=f"Details: {error}", color=nextcord.Color.dark_red())
        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_role("Owner")
    async def download(self, ctx: Context, title: str = None, ver: str = None, link = None, *, description: str):
        embeds = []
        await ctx.message.delete()
        if title == None or ver == None or link == None:
            msg = await ctx.send(f"{ctx.author.mention} You need to specify a title / version / link")
            await asyncio.sleep(5)
            await msg.delete()
            return
        pictures = [p.url for p in ctx.message.attachments]
        embed = nextcord.Embed(title=f"{title} {ver}", description=f"{description}", color=nextcord.Color.brand_green())
        embeds.append(embed)
        embed.add_field(
            name = "Download 🔽",
            value=f"[Click here to download]({link})",
            inline=False
        )
        embed.set_thumbnail(url=self.bot.user.avatar)
        if len(pictures) == 1:
            embed.set_image(url=pictures[0])
        elif len(pictures) > 1:
            for pic in pictures:
                embeds.append(
                    nextcord.Embed(type="image", color=nextcord.Color.brand_green()).set_image(pic)
                )
        embed.set_footer(text=f"Announced by {ctx.author}")
        embed.timestamp = datetime.datetime.now()
        channel = ctx.guild.get_channel(self.d_ch_id)
        await channel.send(embeds=embeds)

    @commands.command()
    @commands.has_any_role("Bot Developer", "Owner")
    async def giverole(self, ctx: Context, role: nextcord.Role, member: nextcord.Member):
        await member.add_roles(role)
        await ctx.send(f"{ctx.author.mention} {role.mention} was given to {member.mention}")

def setup(bot: commands.Bot):
    bot.add_cog(Important(bot))