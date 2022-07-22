from math import perm
from multiprocessing import context
import nextcord, datetime
from nextcord.ext import commands
from nextcord.ext.commands import Context

year = datetime.date.today().year
color = 0xffd500

class Miscellaneous(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(aliases=['latency', 'Ping', 'Latency'], description="Returns the bot's latency")
    async def ping(self, ctx: Context):
        embed = nextcord.Embed(
            color=color,
            title="Ping Pong! 🏓"
        )
        embed.add_field(name='Bot Latency!', value=f"Bot ping is **{round(self.bot.latency * 1000)}ms**", inline=True)
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar)
        embed.set_thumbnail(url=self.bot.user.avatar)
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.timestamp = datetime.datetime.now()
        await ctx.reply(embed=embed)
    
    @commands.command(aliases=['Avatar', 'Av', 'av', 'AVATAR', 'AV', 'PFP', 'pfp', 'Pfp'], description="Returns a user's avatar")
    async def avatar(self, ctx: Context, *, member: nextcord.Member = None):
        if member == None:
            member = ctx.author
        
        if member.avatar is None:
            memberAv = member.default_avatar.url
        else:
            memberAv = member.avatar.url

        embed = nextcord.Embed(title=f"{member.name}'s Avatar", color=color)
        embed.set_image(url=memberAv)
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)
    
    @commands.command(aliases=['serverstats', 'server', 'serverinf', 'servinf'], description="Returns information about the server")
    async def serverinfo(self, ctx: Context):
        embed = nextcord.Embed(color=color)
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

        await ctx.send(f"This is the Server Information ↗ {ctx.author.mention}!", embed=embed)
    

    @commands.command(description="Returns information about a user")
    async def userinfo(self, ctx:Context, *, member: nextcord.Member = None):
        if member is None:
            member = ctx.author
        if member.avatar is None:
            memberAv = member.default_avatar
        else:
            memberAv = member.avatar

        rolelist = [r.mention for r in member.roles if r != ctx.guild.default_role]
        roles = " ".join(rolelist)
        memberRoles = len(member.roles)

        embed = nextcord.Embed(color=color, description=member.mention)
        embed.set_author(name=member.name, icon_url=memberAv)
        embed.set_thumbnail(url=memberAv)

        # perms_to_check = [
        #     "administrator",
        #     "manage_guild",
        #     "manage_roles",
        #     "manage_channels",
        #     "manage_messages",
        #     "manage_webhooks",
        #     "manage_nicknames",
        #     "manage_emojis",
        #     "kick_members",
        #     "ban_members",
        #     "mention_everyone",
        # ]
        # perm_list = nextcord.Permissions()
        # for perm in perms_to_check:
        #     if getattr(member.guild_permissions, perm):
        #         perm_list.update(**{perm: True})


        embed.add_field(name="Joined", value=member.joined_at.strftime('%a, %b %d, %Y %H:%M %p'), inline=True)
        embed.add_field(name="Registered", value=member.created_at.strftime('%a, %b %d, %Y %H:%M %p'), inline=True)
        embed.add_field(name=f"Roles[{memberRoles - 1}]", value=roles, inline=False)
        #embed.add_field(name="Key Permissions", value=perm, inline=False)

        embed.set_footer(text=f"ID: {member.id}")
        embed.timestamp = datetime.datetime.now()

        await ctx.send(embed=embed)


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
