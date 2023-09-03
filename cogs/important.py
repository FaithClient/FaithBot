import discord, asyncio, datetime, requests

from discord.ext import commands, tasks
from discord.ext.pages import PaginatorButton, Paginator, Page
from discord import ApplicationContext as Context

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
        website = requests.get("https://faithclient.vercel.app/", timeout=5)
        try:
            ds = requests.get("https://api.faithclient.tk/anal?authKey=supersecretkey$o_peoplecansee4n3l", timeout=5)
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
    
    @tasks.loop()
    async def autostop(self):
        await self.bot.close()
    
    #@commands.command(aliases=["d"], description="Returns the total downloads of the client")
    @commands.slash_command(description="Returns the total downloads of the client")
    async def downloads(self, ctx: Context):
        ds = requests.get("https://fcapi.manx7.net/anal?authKey=supersecretkey$o_peoplecansee4n3l")
        try:
            counter = ds.json()["downloads"]
            await ctx.respond(f"Downloads: {counter}") #for testing perposes
        except:
            await ctx.respond(f"Download server is offline, so I couldn't get the count...")
    
    @commands.slash_command(description = "Annouces a new faith release!")
    @discord.option(name = "release", type = str)
    @discord.option(name = "description", type = str)
    @discord.option(name = "starting_image", type = discord.Attachment, description = "Set an image for the embed with the text (mandatory)", required = False)
    @discord.option(name = "test_image", type = discord.Attachment, required = False)
    async def announce(self, ctx: discord.ApplicationContext, release: str, description: str, starting_image: discord.Attachment = None, *, test_image: discord.Attachment = None):
        if test_image == None:
            if starting_image == None:
                embed = discord.Embed(
                    title = f"FaithClient v{release} - Release",
                    description = f"{description}\n\n\n[Click here to download/check out our website](https://faithclient.tk)\n\nPlease report any bugs or suggestions to <#1031019801658785895>",
                    color = discord.Color.yellow()
                )
            else:
                embed = discord.Embed(
                    title = f"FaithClient v{release} - Release",
                    description = f"{description}\n\n\n[Click here to download/check out our website](https://faithclient.tk)\n\nPlease report any bugs or suggestions to <#1031019801658785895>",
                    color = discord.Color.yellow()
                ).set_image(url = starting_image.url)
            await ctx.send(embed = embed)
        else:
            i = 0
            buttons = [
                PaginatorButton("first", emoji = "⏪", style = discord.ButtonStyle.green),
                PaginatorButton("prev", emoji = "◀", style = discord.ButtonStyle.green),
                PaginatorButton("page_indicator", style = discord.ButtonStyle.gray, disabled = True),
                PaginatorButton("next", emoji = "▶", style = discord.ButtonStyle.green),
                PaginatorButton("last", emoji = "⏩", style = discord.ButtonStyle.green)
            ]
            pages = [
                Page(
                    embeds = [ 
                        discord.Embed(
                            title = f"FaithClient v{release} - Release",
                            description = f"{description}\n\n\n[Click here to download/check out our website](https://faithclient.tk)\n\nPlease report any bugs or suggestions to <#1031019801658785895>",
                            color = discord.Color.dark_gold(),
                            timestamp = datetime.datetime.now()
                        ).set_footer(text = "Navigate using the buttons below!")
                        if starting_image == None else
                        (discord.Embed(
                            title = f"FaithClient v{release} - Release",
                            description = f"{description}\n\n\n[Click here to download/check out our website](https://faithclient.tk)\n\nPlease report any bugs or suggestions to <#1031019801658785895>",
                            color = discord.Color.dark_gold(),
                            timestamp = datetime.datetime.now()
                        )).set_footer(text = "Navigate using the buttons below!").set_image(url = starting_image.url)
                    ]
                ),  
                Page(
                    embeds = [
                        discord.Embed(
                            type = "image",
                            color = discord.Color.dark_green()
                        ).set_image(url = test_image.url)
                    ]
                )
            ]
            # while i + 1 <= len(test_image):
            #     pages.append(
            #         Page(
            #             embed = (discord.Embed(
            #                 type = "image"
            #             )).set_image(url = test_image.url)
            #         )
            #     )
            #     ++i
            paginator = Paginator(
                pages = pages,
                show_indicator = True,
                use_default_buttons = False,
                custom_buttons = buttons,
                disable_on_timeout = False,
                loop_pages = True
            )
            await paginator.respond(ctx.interaction)

def setup(bot: commands.Bot):
    bot.add_cog(Important(bot))