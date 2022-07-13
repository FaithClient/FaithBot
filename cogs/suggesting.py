import nextcord, asyncio, datetime

from nextcord import utils
from nextcord.ext import commands
from nextcord.ext.commands import Context

class Suggesting(commands.Cog, name="Suggestions"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.s_ch_id = 942179597112475685
    
    # This here is the suggest command; do not uncomment it

    # @commands.command()
    # async def suggest(self, ctx: Context, *, suggestion: str = None):
    #     await ctx.message.delete()
    #     if suggestion == None:
    #         msg = await ctx.send(f"{ctx.author.mention} You need to add a suggestion!!")
    #         await asyncio.sleep(3)
    #         await msg.delete()
    #         return
    #     suggestion_channel = ctx.guild.get_channel(self.s_ch_id)
    #     embed = nextcord.Embed(
    #         description=suggestion,
    #         color = nextcord.Color.green()
    #     )
    #     embed.set_author(
    #         name = f"{ctx.author.name}'s suggestion",
    #         icon_url = ctx.author.avatar if ctx.author.avatar is not None else ctx.author.default_avatar
    #     )
    #     embed.set_thumbnail(
    #         url = self.bot.user.avatar
    #     )
    #     embed.timestamp = datetime.datetime.now()
    #     msg = await suggestion_channel.send(embed=embed)
    #     await msg.add_reaction("⬆")
    #     await msg.add_reaction("⬇")
    #     ans = await ctx.send(f"{ctx.author.mention} Your suggestion was successfully forwarded to {ctx.guild.get_channel(self.s_ch_id).mention}")
    #     await asyncio.sleep(6)
    #     await ans.delete()

    @commands.command(name="delsug", aliases=["ds"])
    async def deletesuggestion(self, ctx: Context, id: int = None):
        if id == None:
            msg = await ctx.send(f"{ctx.author.mention} You need to specify the suggestion's id!")
            await asyncio.sleep(3)
            await msg.delete()
            await ctx.message.delete()
            return
        channel = ctx.guild.get_channel(self.s_ch_id)
        try:
            message = await channel.fetch_message(id)
        except nextcord.NotFound as e:
            print(e)
            msg = await ctx.send(f"{ctx.author.mention} The ID you specified was not a suggestion's ID!!")
            await asyncio.sleep(3)
            await msg.delete()
            await ctx.message.delete()
            return
        await message.delete()
        await message.thread.delete() if message.thread is not None else None
        await ctx.send(f"{ctx.author.mention} The suggestion with ID {id} was successfully deleted!")        

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if message.channel.id == self.s_ch_id:
            if message.author != self.bot.user:
                await message.delete()
                msg = await message.channel.send("Creating suggestion...")
                embed = nextcord.Embed(
                    description=message.content,
                    color = nextcord.Color.green()
                )
                embed.set_author(
                    name = f"{message.author.name}'s suggestion",
                    icon_url = message.author.avatar if message.author.avatar is not None else message.author.default_avatar
                )
                embed.set_thumbnail(
                    url = self.bot.user.avatar
                )
                embed.set_footer(
                    text = f"ID: {msg.id}"
                )
                embed.timestamp = datetime.datetime.now()
                await msg.edit(content=None, embed=embed)
                await msg.add_reaction("⬆")
                await msg.add_reaction("⬇")
                await msg.create_thread(
                    name = f"Discussion of suggestion with ID {msg.id}"
                )
                await message.author.send(f"{message.author.mention} Your suggestion was successfully forwarded to {message.guild.get_channel(self.s_ch_id).mention}")

def setup(bot: commands.Bot):
    bot.add_cog(Suggesting(bot))