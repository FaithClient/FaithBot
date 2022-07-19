import nextcord, asyncio, datetime, requests, re, time

from nextcord.ext import commands, tasks
from nextcord.ext.commands import Context

class Important(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.d_ch_id = 942179597112475678
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx: Context, error: Exception):
        embed = nextcord.Embed(title="An exception was raised", description=f"Details: {error}", color=nextcord.Color.dark_red())
        await ctx.send(embed=embed)
    
    @commands.command(aliases=["swt", "sendwt"], description="Starts the web status task")
    @commands.has_any_role("Owner", "Bot Developer")
    async def send_webtask(self, ctx: Context):
        msg = await ctx.send("Starting task...")
        self.webtask.start(msg)
        await ctx.message.delete()
    
    @tasks.loop(seconds=5)
    async def webtask(self, msg: nextcord.Message):
        async def countdown(t: int, message: nextcord.Message):
            membed = message.embeds[0]
            while t >= 0:
                membed.set_footer(text=f"Updating in {t} second(s)")
                await message.edit(content=None, embed=membed)
                await asyncio.sleep(1)
                t -= 1
        ds = requests.get("https://fcapi.manx7.net/anal", timeout=5)
        website = requests.get("https://faithclient.vercel.app/", timeout=5)
        try:
            ds = ds.json()
            dss = ds["amOnline"]
            dc = ds["downloads"]
            ws = website.status_code
            embed = nextcord.Embed(color=nextcord.Color.dark_green())
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
                embed.color = nextcord.Color.dark_orange()
            elif ws >= 500:
                embed.add_field(
                    name = "Website Status",
                    value = f"🔴 Server error (Code: {ws})",
                    inline = False
                )
                embed.color = nextcord.Color.dark_red()
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
            await countdown(5, final)
        except:
            embed = nextcord.Embed(color=nextcord.Color.dark_red())
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
            await countdown(5, final)

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
    
    # @commands.command(aliases=["wb"])
    # async def webstatus(self, ctx: Context):
    #     ds = requests.get("https://fcapi.manx7.net/anal", timeout=6)
    #     website = requests.get("https://faithclient.vercel.app/", timeout=6)
    #     try:
    #         ds = ds.json()
    #         dss = ds["amOnline"]
    #         dc = ds["downloads"] # This is actually for the download counter, wrong command woops
    #         ws = website.status_code
    #         embed = nextcord.Embed(color=nextcord.Color.dark_green())
    #         if ws == 200:
    #             embed.add_field(
    #                 name = "Website Status",
    #                 value = "🟢 Up and running",
    #                 inline = False
    #             )
    #         elif ws >= 400 and ws < 500:
    #             embed.add_field(
    #                 name = "Website Status",
    #                 value = f"🟠 Client error (Code: {ws})",
    #                 inline = False
    #             )
    #             embed.color = nextcord.Color.dark_orange()
    #         elif ws >= 500:
    #             embed.add_field(
    #                 name = "Website Status",
    #                 value = f"🔴 Server error (Code: {ws})",
    #                 inline = False
    #             )
    #             embed.color = nextcord.Color.dark_red()
    #         embed.add_field(
    #             name = "Download Server Status",
    #             value = "🟢 Up and running", 
    #             inline = False
    #         )
    #         embed.set_author(
    #             name = "FaithBot",
    #             icon_url = self.bot.user.avatar
    #         )
    #         embed.timestamp = datetime.datetime.now()
    #         await ctx.send(embed=embed)
    #     except:
    #         embed = nextcord.Embed(color=nextcord.Color.dark_red())
    #         ws = website.status_code
    #         if ws == 200:
    #             embed.add_field(
    #                 name = "Website Status",
    #                 value = "🟢 Up and running",
    #                 inline = False
    #             )
    #         elif ws >= 400 and ws < 500:
    #             embed.add_field(
    #                 name = "Website Status",
    #                 value = f"🟠 Client error (Code: {ws})",
    #                 inline = False
    #             )
    #         elif ws >= 500:
    #             embed.add_field(
    #                 name = "Website Status",
    #                 value = f"🔴 Server error (Code: {ws})",
    #                 inline = False
    #             )

    #         embed.add_field(
    #             name = "Download Server Status",
    #             value = "🔴 Offline",
    #             inline = False
    #         )
    #         embed.set_author(
    #             name = "FaithBot",
    #             icon_url = self.bot.user.avatar
    #         )
    #         embed.timestamp = datetime.datetime.now()
    #         await ctx.send(embed=embed)
    
    @commands.command(aliases=["d"], description="Returns the total downloads of the client")
    async def downloads(self, ctx: Context):
        ds = requests.get("https://fcapi.manx7.net/anal")
        try:
            counter = ds.json()["downloads"]
            await ctx.send(f"Downloads: {counter}") #for testing perposes
        except:
            await ctx.send(f"Download server is offline, so I couldn't get the count...")

    @commands.command(description="Gives a role to a user")
    @commands.has_any_role("Bot Developer", "Owner")
    async def giverole(self, ctx: Context, role: nextcord.Role, member: nextcord.Member):
        await member.add_roles(role)
        await ctx.send(f"{ctx.author.mention} {role.mention} was given to {member.mention}")

def setup(bot: commands.Bot):
    bot.add_cog(Important(bot))