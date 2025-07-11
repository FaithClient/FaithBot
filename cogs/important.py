import discord, asyncio, datetime, requests

from discord.ext import commands, tasks
from discord.ext.pages import PaginatorButton, Paginator, Page
from discord import ApplicationContext as Context

color = 0xffd500 # Embed color
chid = 1148734231527313509 # Channel id for announcements

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
        website = requests.get("https://faithclient.tech/", timeout=5)
        try:
            ds = requests.get("https://server.faithclient.tech/anal?authKey=supersecretkey$o_peoplecansee4n3l", timeout=5)
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
    
    @commands.slash_command(description="Returns the total downloads of the client")
    async def downloads(self, ctx: Context):
        ds = requests.get("https://server.faithclient.tech/anal?authKey=supersecretkey$o_peoplecansee4n3l")
        try:
            counter = ds.json()["downloads"]
            await ctx.respond(f"Downloads: {counter}") #for testing perposes
        except:
            await ctx.respond(f"Download server is offline, so I couldn't get the count...")
    
    @commands.slash_command(description = "Prepares an announcement of a new FaithClient release!")
    # @discord.option(name = "release", type = str)
    # @discord.option(name = "description", type = str)
    # @discord.option(name = "starting_image", type = discord.Attachment, description = "Set an image for the embed with the text (mandatory)", required = False)
    # @discord.option(name = "test_image", type = discord.Attachment, required = False)
    # async def announce(self, ctx: discord.ApplicationContext, release: str, description: str, starting_image: discord.Attachment = None, *, test_image: discord.Attachment = None):
    #     if test_image == None:
    #         if starting_image == None:
    #             embed = discord.Embed(
    #                 title = f"FaithClient v{release} - Release",
    #                 description = f"{description}\n\n\n[Click here to download/check out our website](https://faithclient.tech)\n\nPlease report any bugs or suggestions to <#1031019801658785895>",
    #                 color = discord.Color.yellow()
    #             )
    #         else:
    #             embed = discord.Embed(
    #                 title = f"FaithClient v{release} - Release",
    #                 description = f"{description}\n\n\n[Click here to download/check out our website](https://faithclient.tech)\n\nPlease report any bugs or suggestions to <#1031019801658785895>",
    #                 color = discord.Color.yellow()
    #             ).set_image(url = starting_image.url)
    #         await ctx.send(embed = embed)
    #     else:
    #         i = 0
    #         buttons = [
    #             PaginatorButton("first", emoji = "⏪", style = discord.ButtonStyle.green),
    #             PaginatorButton("prev", emoji = "◀", style = discord.ButtonStyle.green),
    #             PaginatorButton("page_indicator", style = discord.ButtonStyle.gray, disabled = True),
    #             PaginatorButton("next", emoji = "▶", style = discord.ButtonStyle.green),
    #             PaginatorButton("last", emoji = "⏩", style = discord.ButtonStyle.green)
    #         ]
    #         pages = [
    #             Page(
    #                 embeds = [ 
    #                     discord.Embed(
    #                         title = f"FaithClient v{release} - Release",
    #                         description = f"{description}\n\n\n[Click here to download/check out our website](https://faithclient.tech)\n\nPlease report any bugs or suggestions to <#1031019801658785895>",
    #                         color = discord.Color.dark_gold(),
    #                         timestamp = datetime.datetime.now()
    #                     ).set_footer(text = "Navigate using the buttons below!")
    #                     if starting_image == None else
    #                     (discord.Embed(
    #                         title = f"FaithClient v{release} - Release",
    #                         description = f"{description}\n\n\n[Click here to download/check out our website](https://faithclient.tech)\n\nPlease report any bugs or suggestions to <#1031019801658785895>",
    #                         color = discord.Color.dark_gold(),
    #                         timestamp = datetime.datetime.now()
    #                     )).set_footer(text = "Navigate using the buttons below!").set_image(url = starting_image.url)
    #                 ]
    #             ),  
    #             Page(
    #                 embeds = [
    #                     (discord.Embed(
    #                         type = "image",
    #                         color = discord.Color.dark_green(),
    #                         timestamp = datetime.datetime.now()
    #                     )).set_image(url = test_image.url).set_footer(text = "Navigate using the buttons below!")
    #                 ]
    #             )
    #         ]
    #         # while i + 1 <= len(test_image):
    #         #     pages.append(
    #         #         Page(
    #         #             embed = (discord.Embed(
    #         #                 type = "image"
    #         #             )).set_image(url = test_image.url)
    #         #         )
    #         #     )
    #         #     ++i
    #         paginator = Paginator(
    #             pages = pages,
    #             show_indicator = True,
    #             use_default_buttons = False,
    #             custom_buttons = buttons,
    #             disable_on_timeout = False,
    #             loop_pages = True
    #         )
    #         await paginator.respond(ctx.interaction)
    async def announce(self, ctx: discord.ApplicationContext):
        pictures = []
        await ctx.defer()
        # Information gathering
        channel = ctx.channel
        author = ctx.author
        def check(m: discord.Message):
            return m.channel == channel and m.author == author

        msg1 = await ctx.send("[!] Answer the following questions to give the bot the required information for the announcement to be built.")
        msg2 = await ctx.send("[+] What version are we releasing?")
        ans1 = await self.bot.wait_for("message", check=check)
        release = ans1.content
        await ans1.delete()

        await msg2.edit(f"[+] v{release} it is. Write down a description for the announcement.")
        ans2 = await self.bot.wait_for("message", check=check)
        description = ans2.content
        await ans2.delete()

        await msg2.edit("[+] Great! Attach the front-page picture...")
        ans3 = await self.bot.wait_for("message", check=check)
        front_image = ans3.attachments
        await ans3.delete()

        await msg2.edit("[+] ...and pictures for the other pages.")
        ans4 = await self.bot.wait_for("message", check=check)
        page_images = ans4.attachments
        await ans4.delete()

        await msg2.delete()
        await msg1.delete()
        message = await ctx.send(content = "[!] Alright, here's the data you've given me:", embed=(discord.Embed(
            colour = discord.Color.yellow(),
            title = "Data"
        )).add_field(name = "Release", value = f"{release}", inline = False)
        .add_field(name = "Description", value = description, inline = False)
        .add_field(name = "Front image", value = "Selected" if len(front_image) == 1 else "Not selected")
        .add_field(name = "Page images", value = f"({len(page_images)}) Selected" if len(page_images) > 0 else "Not selected"))
        warning = await ctx.send("[!] Is that all? (y/Y/yes for yes | n/N/no for no)")
        answer = await self.bot.wait_for("message", check=check)
        pictures.insert(0, front_image)
        i = 1
        while i <= len(page_images):
            pictures.insert(i, page_images[i-1])
            i += 1
        async def corrections(answer: discord.Message, msg: discord.Message, pictures: list):
            match answer.content:
                case "yes" | "Y" | "y":
                    await answer.delete()
                    await warning.edit("[!] Alright, creating the announcement, please wait")
                case "no" | "N" | "n": #WIP
                    await answer.delete()
                    fembed = msg.embeds[0]
                    fields = fembed.fields
                    async def no(warning: discord.Message):
                        await warning.edit("[!] What would you like to change?\n\t1 -> Release number\n\t2 -> Description\n\t3 -> Front image\n\t4 -> Page image(s)\n\t5 -> Cancel\n\t6 -> Stop command")
                        ans = await self.bot.wait_for("message", check=check)
                        match ans.content:
                            case "1":
                                await ans.delete()
                                await warning.edit("[+] Alright, give me a new release number")
                                ans = await self.bot.wait_for("message", check=check)
                                release = ans.content
                                await ans.delete()
                                field = fields[0]
                                field.value = release
                                await msg.edit(embed=fembed)
                                await warning.edit("[!] Is that all? (y/Y/yes for yes | n/N/no for no)")
                                answer = await self.bot.wait_for("message", check=check)
                                await corrections(answer, message, pictures)
                            case "2":
                                await ans.delete()
                                await warning.edit("[+] Alright, give me a new description")
                                ans = await self.bot.wait_for("message", check=check)
                                description = ans.content
                                await ans.delete()
                                field = fields[1]
                                field.value = description
                                await msg.edit(embed=fembed)
                                await warning.edit("[!] Is that all? (y/Y/yes for yes | n/N/no for no)")
                                answer = await self.bot.wait_for("message", check=check)
                                await corrections(answer, message, pictures)
                            case "3":
                                await ans.delete()
                                await warning.edit("[+] Alright, give me a new front-page image")
                                ans = await self.bot.wait_for("message", check=check)
                                pictures[0] = ans.attachments
                                await ans.delete()
                                field = fields[2]
                                field.value = "Selected" if len(ans.attachments) == 1 else "Not selected"
                                await msg.edit(embed=fembed)
                                await warning.edit("[!] Is that all? (y/Y/yes for yes | n/N/no for no)")
                                answer = await self.bot.wait_for("message", check=check)
                                await corrections(answer, message, pictures)
                            case "4":
                                await ans.delete()
                                await warning.edit("[+] Alright, give me new page images")
                                ans = await self.bot.wait_for("message", check=check)
                                if len(ans.attachments) > 0:
                                    i = 1
                                    while i <= len(ans.attachments):
                                        pictures[i] = ans.attachments[i-1]
                                        i += 1
                                else:
                                    i = len(pictures - 1)
                                    while i >= len(pictures - 1) and i != 0:
                                        pictures.remove(i)
                                        i -= 1
                                await ans.delete()
                                field = fields[3]
                                field.value = f"({len(ans.attachments)}) Selected" if len(ans.attachments) > 0 else "Not selected"
                                await msg.edit(embed=fembed)
                                await warning.edit("[!] Is that all? (y/Y/yes for yes | n/N/no for no)")
                                answer = await self.bot.wait_for("message", check=check)
                                await corrections(answer, message, pictures)
                            case "5":
                                await ans.delete()
                                await warning.edit("[!] Alright, creating the announcement, please wait")
                            case "6":
                                await ans.delete()
                                await warning.edit("[!] Alright, cancelling process...")
                                await asyncio.sleep(2)
                                return "cancel"
                            case _:
                                await ans.delete()
                                await warning.edit("[!] Wrong option, repeating process...")
                                await asyncio.sleep(1)
                                await no(warning)
                    return await no(warning)
                case _:
                    await answer.delete()
                    await warning.edit("[!] Wrong option, repeating process...")
                    await asyncio.sleep(1)
                    await warning.edit("[!] Is that all? (y/Y/yes for yes | n/N/no for no)")
                    answer = await self.bot.wait_for("message", check=check)
                    await corrections(answer, message, pictures)
            return pictures
        a = await corrections(answer, message, pictures)
        if a == "cancel":
            await warning.delete()
            await message.delete()
            return
        elif a != None:
            a = pictures

        # Final data
        emb = message.embeds[0]
        fields = emb.fields
        release = fields[0].value[0]
        description = fields[1].value
        try: front_image = pictures[0]
        except: front_image = []
        try: page_images = pictures[1:]
        except: page_images = []

        # Paginator
        if len(page_images) == 0:
            embed = discord.Embed(
                title = f"FaithClient v{release} - Release",
                description = f"{description}\n\n[Click here to download/check out our website](https://faithclient.tech)\n[View our Terms of Service](https://faithclient.tech/tos)\n\nPlease report any bugs or suggestions to <#1031019801658785895>",
                color = color
            )
            if len(front_image) != 0:
                file = front_image[0]
                embed.set_image(url = file.url)
            embed.set_author(name = "FaithClient Team", icon_url = self.bot.user.avatar.url)
            await warning.delete()
            await message.delete()
            await ctx.delete()
            channel = self.bot.get_channel(chid)
            await channel.send(embed=embed)
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
                        (discord.Embed(
                            title = f"FaithClient v{release} - Release",
                            description = f"{description}\n\n[Click here to download/check out our website](https://faithclient.tech)\n[View our Terms of Service](https://faithclient.tech/tos)\n\nPlease report any bugs or suggestions to <#1031019801658785895>",
                            color = color,
                            timestamp = datetime.datetime.now()
                        )).set_footer(text = "Navigate using the buttons below!").set_author(name = "FaithClient Team", icon_url = self.bot.user.avatar.url)
                        if len(front_image) == 0 else
                        (discord.Embed(
                            title = f"FaithClient v{release} - Release",
                            description = f"{description}\n\n[Click here to download/check out our website](https://faithclient.tech)\n[View our Terms of Service](https://faithclient.tech/tos)\n\nPlease report any bugs or suggestions to <#1031019801658785895>",
                            color = color
                            ,
                            timestamp = datetime.datetime.now()
                        )).set_footer(text = "Navigate using the buttons below!").set_image(url = front_image[0].url).set_author(name = "FaithClient Team", icon_url = self.bot.user.avatar.url)
                    ]
                )
            ]

            while i + 1 <= len(page_images):
                image = page_images[i]
                pages.append((discord.Embed(
                    type = "image",
                    timestamp = datetime.datetime.now(),
                    color = color
                ).set_image(url = image.url).set_footer(text = "Navigate using the buttons below!")))
                i += 1
            
            paginator = Paginator(
                pages = pages,
                show_indicator = True,
                use_default_buttons = False,
                custom_buttons = buttons,
                disable_on_timeout = False,
                loop_pages = True
            )
            await warning.delete()
            await message.delete()
            await paginator.respond(ctx.interaction, target = self.bot.get_channel(1148734231527313509), target_message = "Sent!") # ISSUES HERE
    
    @commands.slash_command()
    @discord.option(name = "number", type = int, description = "The number of messages you want to delete.", required = True, min_value = 1)
    @discord.commands.default_permissions(manage_messages = True)
    async def purge(self, ctx: Context, number: int):
        final_num = 0
        msges = await ctx.channel.purge(limit = number)
        for msg in msges:
            final_num += 1
        await ctx.respond(f"[{ctx.author.mention}] Deleted {final_num} message(s).", delete_after = 4.0)

def setup(bot: commands.Bot):
    bot.add_cog(Important(bot))