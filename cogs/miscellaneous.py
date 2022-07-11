import nextcord, datetime

from PIL import Image
from io import BytesIO
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

    # @commands.command()
    # async def wantedTest(self, ctx: Context, *, member: nextcord.Member = None):
    #     if member == None:
    #         member = ctx.author
    #     wanted = Image.open("./assets/wanted.png")
    #     asset = member.avatar.with_size(128)
    #     data = BytesIO(await asset.read())
    #     pfp = Image.open(data)
    #     pfp = pfp.resize((177, 177))

    #     wanted.paste(pfp, (120, 212))
    #     wanted.save("./assets/profile.jpg")

    #     await ctx.send(file = nextcord.File("./assets/profile.jpg"))

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        embed = nextcord.Embed(color=color, description="‎\n**Sexo**\n- Bedezu")
        embed.set_footer(text=f"Requested by {message.author} | 😳")
        embed.set_thumbnail(url='https://cdn.shopify.com/s/files/1/1061/1924/products/Flushed_Emoji_Icon_5e6ce936-4add-472b-96ba-9082998adcf7_grande.png')
        embed.timestamp = datetime.datetime.now()
        if message.content.startswith("sexo") or message.content.startswith("Sexo"):
            await message.reply(embed=embed) 

def setup(bot: commands.Bot):
    bot.add_cog(Miscellaneous(bot))
