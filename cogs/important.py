from pydoc import describe
import discord, asyncio, datetime, requests

from discord.ext import commands, tasks
from discord.ext.commands import Context

bot = commands.Bot

class Important(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.d_ch_id = 942179597112475678
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx: Context, error: Exception):
        embed = discord.Embed(title="An exception was raised", description=f"Details: {error}", color=discord.Color.dark_red())
        await ctx.send(embed=embed)
    
    @commands.command(aliases=["swt", "sendwt"], description="Starts the web status task")
    @commands.has_any_role("Owner", "Bot Developer")
    async def send_webtask(self, ctx: Context):
        msg = await ctx.send("Starting task...")
        self.webtask.start(msg)
        await ctx.message.delete()
    
    @tasks.loop(seconds=60)
    async def webtask(self, msg: discord.Message):
        async def countdown(t: int, message: discord.Message):
            membed = message.embeds[0]
            while t >= 0:
                membed.set_footer(text=f"Updating in {t} second(s)")
                await message.edit(content=None, embed=membed)
                await asyncio.sleep(1)
                t -= 1
        ds = requests.get("https://fcapi.manx7.net/anal?authKey=supersecretkey$o_peoplecansee4n3l", timeout=5)
        website = requests.get("https://faithclient.vercel.app/", timeout=5)
        try:
            ds = ds.json()
            dss = ds["amOnline"]
            dc = ds["downloads"]
            ws = website.status_code
            embed = discord.Embed(color=discord.Color.dark_green())
            if ws == 200:
                embed.add_field(
                    name = "Website Status",
                    value = "🟢 Up and running",
                    inline = False
                )
            elif ws >= 400 and ws < 500:
                embed.add_field(
                    name = "Website Status",
                    value = f"🟠 Client error (Code: {ws})",
                    inline = False
                )
                embed.color = discord.Color.dark_orange()
            elif ws >= 500:
                embed.add_field(
                    name = "Website Status",
                    value = f"🔴 Server error (Code: {ws})",
                    inline = False
                )
                embed.color = discord.Color.dark_red()
            embed.add_field(
                name = "Download Server Status",
                value = "🟢 Up and running", 
                inline = False
            )
            embed.add_field(
                name = "Downloads",
                value = dc,
                inline = False
            )
            embed.set_author(
                name = "FaithBot",
                icon_url = self.bot.user.avatar
            )
            embed.set_thumbnail(url=msg.guild.icon)
            embed.timestamp = datetime.datetime.now()
            embed.set_footer(text="Updating in 0 second(s)")
            final = await msg.edit(content=None, embed=embed)
            await countdown(60, final)
        except:
            embed = discord.Embed(color=discord.Color.dark_red())
            ws = website.status_code
            if ws == 200:
                embed.add_field(
                    name = "Website Status",
                    value = "🟢 Up and running",
                    inline = False
                )
            elif ws >= 400 and ws < 500:
                embed.add_field(
                    name = "Website Status",
                    value = f"🟠 Client error (Code: {ws})",
                    inline = False
                )
            elif ws >= 500:
                embed.add_field(
                    name = "Website Status",
                    value = f"🔴 Server error (Code: {ws})",
                    inline = False
                )

            embed.add_field(
                name = "Download Server Status",
                value = "🔴 Offline",
                inline = False
            )
            embed.set_author(
                name = "FaithBot",
                icon_url = self.bot.user.avatar
            )
            embed.set_thumbnail(url=msg.guild.icon)
            embed.timestamp = datetime.datetime.now()
            embed.set_footer(text="Updating in 0 second(s)")
            final = await msg.edit(content=None, embed=embed)
            await countdown(60, final)

    @commands.command(description="Sends a download announcement to <#942179597112475678>")
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
        embed = discord.Embed(title=f"{title} {ver}", description=f"{description}", color=discord.Color.brand_green())
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
                    discord.Embed(type="image", color=discord.Color.brand_green()).set_image(pic)
                )
        embed.set_footer(text=f"Announced by {ctx.author}")
        embed.timestamp = datetime.datetime.now()
        channel = ctx.guild.get_channel(self.d_ch_id)
        msg = await channel.send(embeds=embeds)
        # if len(pictures) == 1:
        #     await msg.add_reaction("◀")
        #     await msg.add_reaction("▶")

    # @commands.Cog.listener()
    # async def on_reaction_add(self, reaction: discord.Reaction, user: discord.Member):
    #     # if reaction.emoji == "▶" and self.bot.user in reaction.users().flatten():
    #     #     if user != self.bot.user:
    #     #         await reaction.remove()
    #     #         message = reaction.message
    #     #         embed = message.embeds[0]
    #     #         title = embed.title
    #     #         desc = embed.description
    #     #         timestamp = embed.timestamp
    #     #         pictures = [p.url for p in message.attachments]
    #     if reaction.emoji == "🔴" and reaction.message.channel.id == 942179597112475685:
    #         await reaction.message.edit(content="❌ Denied", embeds=reaction.message.embeds)

    
    @commands.command(aliases=["d"], description="Returns the total downloads of the client")
    async def downloads(self, ctx: Context):
        ds = requests.get("https://fcapi.manx7.net/anal?authKey=supersecretkey$o_peoplecansee4n3l")
        try:
            counter = ds.json()["downloads"]
            await ctx.send(f"Downloads: {counter}") #for testing perposes
        except:
            await ctx.send(f"Download server is offline, so I couldn't get the count...")

    @commands.command(description="Gives a role to a user")
    @commands.has_any_role("Bot Developer", "Owner")
    async def giverole(self, ctx: Context, role: discord.Role, member: discord.Member):
        await member.add_roles(role)
        await ctx.send(f"{ctx.author.mention} {role.mention} was given to {member.mention}")

#     #This is a test command
#     @commands.command(description="A command to test the UI features of pycord")
#     @commands.has_any_role("Owner", "Bot Developer")
#     async def testui(self, ctx: Context):
#         att = ctx.message.attachments
#         if len(att) != 0:
#             pictures = [p.url for p in att]
#         else:
#             warning = await ctx.send("Attach some pictures")
#             await asyncio.sleep(3)
#             await warning.delete()
#             return
#         embed = discord.Embed(
#             title = "Testing...",
#             color = discord.Color.green(),
#             type = "image"
#         )
#         embed.set_image(url=pictures[0])
#         if len(pictures) > 0:
#             await ctx.send(embed=embed, view=TestView())
#         else:
#             await ctx.send(embed=embed)
            
# #This is a test view class
# class TestView(discord.ui.View):
#     @discord.ui.button(label="Swap!", style=discord.ButtonStyle.primary, emoji="➡")
#     async def button_swap(self, button: discord.ui.Button, interaction: discord.Interaction):
#         context = await bot.get_context(bot, self.message)
#         embed = self.message.embeds[0]
#         att = context
#         pictures = [p.url for p in att]
#         if len(att) > 0:
#             embed_picture = embed.image.url
#             try:
#                 index = pictures.index(embed_picture) + 1
#             except ValueError as e:
#                 await interaction.response.send_message("An error occurred, check console for more details")
#                 print("Exception: " + e)
#             try:
#                 embed.image.url = pictures[index]
#                 await self.message.edit(embed=embed, view=self)
#             except Exception as e:
#                 await interaction.response.send_message("An error occurred, check console for more details")
#                 print("Exception: " + e)
#         else: return

def setup(bot: commands.Bot):
    bot.add_cog(Important(bot))