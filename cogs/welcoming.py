import discord, datetime

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from discord.ext import commands
from discord.ext.commands import Context

welcome_channel_id = 942179597112475681
year = datetime.date.today().year
color = 0xffd500

class Welcoming(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):

        embed = discord.Embed(color=color)
        W,H = (320, 498)

        leave = Image.open("./assets/leaving.png")
        draw = ImageDraw.Draw(leave)
        font = ImageFont.truetype("./assets/Raleway-Regular.ttf", 23)

        if member.avatar is None:
            asset = member.default_avatar.with_size(128)
        else:
            asset = member.avatar.with_size(128)

        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((135, 135))

        text = f"{member.name}#{member.display_name}"
        leave.paste(pfp, (92, 77))
        text_width = font.getlength(text)
        w,h = text_width, font.size
        draw.text(((W-w)/2, (H-h)/2), text, (255, 255, 255), font=font)

        leave.save("./assets/profile.png")
        embed.set_image(url="attachment://profile.png")

        await member.guild.get_channel(welcome_channel_id).send(f"Goodbye, {member.mention}. We hope you enjoyed your stay here.", file = discord.File("./assets/profile.png"), embed=embed)


    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):

        embed = discord.Embed(color=color)
        W,H = (320, 498)

        welcome = Image.open("./assets/welcome.png")
        draw = ImageDraw.Draw(welcome)
        font = ImageFont.truetype("./assets/Raleway-Regular.ttf", 23)

        if member.avatar is None:
            asset = member.default_avatar.with_size(128)
        else:
            asset = member.avatar.with_size(128)

        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((135, 135))

        text = f"{member.name}#{member.display_name}"
        welcome.paste(pfp, (92, 77))
        text_width = font.getlength(text)
        w,h = text_width, font.size
        draw.text(((W-w)/2, (H-h)/2), text, (255, 255, 255), font=font)

        welcome.save("./assets/profile.png")
        embed.set_image(url="attachment://profile.png")

        await member.guild.get_channel(welcome_channel_id).send(f"""Welcome to the FaithClient Discord, {member.mention}
Please read the rules at <#942179596718186554>, and you can download the client at <#942179597112475678>
""", file = discord.File("./assets/profile.png"), embed=embed)


#     @commands.command(aliases=["welcome"], description="This is just a test command lol")
#     @commands.has_any_role("Owner", "Bot Developer")
#     async def welcometest(self, ctx: Context, *, member: discord.Member = None):
#         if member == None:
#             member = ctx.author

#         embed = discord.Embed(color=color)
#         W,H = (320, 498)

#         welcome = Image.open("./assets/welcome.png")
#         draw = ImageDraw.Draw(welcome)
#         font = ImageFont.truetype("./assets/Raleway-Regular.ttf", 23)

#         if member.avatar is None:
#             asset = member.default_avatar.with_size(128)
#         else:
#             asset = member.avatar.with_size(128)

#         data = BytesIO(await asset.read())
#         pfp = Image.open(data)
#         pfp = pfp.resize((135, 135))

#         text = f"{member.name}#{member.discriminator}"
#         welcome.paste(pfp, (92, 77))
#         text_width = font.getlength(text)
#         w,h = text_width, font.size
#         draw.text(((W-w)/2, (H-h)/2), text, (255, 255, 255), font=font)

#         welcome.save("./assets/profile.png")
#         embed.set_image(url="attachment://profile.png")

#         await ctx.send(f"""Welcome to the FaithClient Discord, {member.mention}
# Please read the rules at <#942179596718186554>, and you can download the client at <#942179597112475678>. 
#             """, file = discord.File("./assets/profile.png"), 
#         embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Welcoming(bot))
