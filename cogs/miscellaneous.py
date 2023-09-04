import discord, datetime, requests, json
from discord import ApplicationContext as Context
from discord import Option
from discord.ext import commands

year = datetime.date.today().year
color = 0xffd500

class Miscellaneous(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command(description = "Returns the bot's latency")
    async def ping(self, ctx: Context):
        embed = discord.Embed(
            color=color,
            title="Ping Pong! 🏓"
        )
        embed.add_field(
            name='Bot Latency!', 
            value=f"Bot ping is **{round(self.bot.latency * 1000)}ms**", 
            inline=True
        )
        embed.set_author(
            name=self.bot.user, 
            icon_url=self.bot.user.avatar
        )
        embed.set_thumbnail(url=self.bot.user.avatar)
        embed.set_footer(text=f"Requested by {ctx.author.display_name}")
        embed.timestamp = datetime.datetime.now()
        await ctx.respond(embed=embed)
    
    @commands.slash_command(description="Returns a user's avatar")
    async def avatar(self, ctx: Context, member: Option(discord.Member, name = "member", description = "Who's avatar do you want?", required = False)):
        if member == None:
            member = ctx.author
        
        if member.avatar is None:
            memberAv = member.default_avatar.url
        else:
            memberAv = member.avatar.url

        embed = discord.Embed(
            title=f"{member.name}'s Avatar", 
            color=color
        )
        embed.set_image(url=memberAv)
        embed.set_footer(text=f"Requested by {ctx.author.display_name}")
        embed.timestamp = datetime.datetime.now()
        await ctx.respond(embed=embed)
    
    @commands.slash_command(description="Returns information about the server")
    async def serverinfo(self, ctx: Context):
        embed = discord.Embed(color=color)
        role_count = len(ctx.guild.roles)
        role_count -= 1

        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
        embed.set_thumbnail(url=ctx.guild.icon.url)

        embed.add_field(name="Owner", value=ctx.guild.owner, inline=True)
        embed.add_field(name="Category Channels", value=len(ctx.guild.categories), inline=True)
        embed.add_field(name="Text Channels", value=len(ctx.guild.text_channels), inline=True)
        embed.add_field(name="Voice Channels", value=len(ctx.guild.voice_channels), inline=True)
        embed.add_field(name="Members", value=ctx.guild.member_count, inline=True)
        embed.add_field(name="Roles", value=str(role_count), inline=True)
    
        embed.set_footer(text=f"ID: {ctx.guild.id} | Server Created • {ctx.guild.created_at.__format__('%d/%m/%y')}")

        await ctx.respond(f"This is the Server Information ↗ {ctx.author.mention}!", embed=embed)
    

    @commands.slash_command(description="Returns information about a user")
    async def userinfo(self, ctx: Context, member: Option(discord.Member, name = "member", description = "Who's profile do you want to check?", required = False)):
        if member is None:
            member = ctx.author
        if member.avatar is None:
            memberAv = member.default_avatar
        else:
            memberAv = member.avatar

        rolelist = [r.mention for r in member.roles if r != ctx.guild.default_role]
        roles = " ".join(rolelist)
        memberRoles = len(member.roles)

        embed = discord.Embed(color=color, description=member.mention)
        embed.set_author(name=member.name, icon_url=memberAv)
        embed.set_thumbnail(url=memberAv)

        embed.add_field(name="Joined", value=member.joined_at.strftime('%a, %b %d, %Y %H:%M %p'), inline=True)
        embed.add_field(name="Registered", value=member.created_at.strftime('%a, %b %d, %Y %H:%M %p'), inline=True)
        embed.add_field(name=f"Roles[{memberRoles - 1}]", value=roles, inline=False)

        embed.set_footer(text=f"ID: {member.id}")
        embed.timestamp = datetime.datetime.now()

        await ctx.respond(embed=embed)


    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        msg_cnt = message.content.lower()
        if msg_cnt.__contains__("sexo"):
            embed = discord.Embed(color=discord.Color.yellow())
            embed.add_field(
                name = "\n\n\nSexo",
                value = "\- Bedezu",
                inline = False
            )
            embed.set_thumbnail(url="https://cdn.emojidex.com/emoji/seal/flushed1.png?1605449223")
            embed.set_footer(
                text = f"Requested by {message.author.display_name} | 😳"
            )
            embed.timestamp = datetime.datetime.now()
            await message.reply(embed=embed)
    
    
    @commands.slash_command(description="Sends random meme")
    async def meme(self, ctx: Context):
        await ctx.defer()
        r = requests.get(f"https://api.pymeme.repl.co/random/")
        data = r.json()
        memechoice: str = data['meme']['image url']
        embed = discord.Embed (
            title=data['meme']['title'],
            description=f"Author: {data['meme']['author']}",
            color=color
        )
        embed.set_image(url=memechoice)
        embed.set_author(
            name=self.bot.user.display_name, 
            icon_url=self.bot.user.avatar
        )
        embed.add_field(
            name='Upvotes:', 
            value=data['meme']['upvotes'], 
            inline=True
        )
        embed.add_field(
            name='Original Post:', 
            value=data['meme']['post url'], 
            inline=True
        )
        embed.set_footer(text = f"Requested by {ctx.author.display_name}")
        embed.timestamp = datetime.datetime.now()
        await ctx.respond(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Miscellaneous(bot))