import discord, datetime
from discord.ext import commands
from discord.ext.commands import Context

year = datetime.date.today().year
color = 0xffd500

class Miscellaneous(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(aliases=['latency', 'Ping', 'Latency'], description="Returns the bot's latency", usage="`ft!ping`")
    async def ping(self, ctx: Context):
        embed = discord.Embed(
            color=color,
            title="Ping Pong! 🏓"
        )
        embed.add_field(name='Bot Latency!', value=f"Bot ping is **{round(self.bot.latency * 1000)}ms**", inline=True)
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar)
        embed.set_thumbnail(url=self.bot.user.avatar)
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.timestamp = datetime.datetime.now()
        await ctx.reply(embed=embed)
    
    @commands.command(aliases=['Avatar', 'Av', 'av', 'AVATAR', 'AV', 'PFP', 'pfp', 'Pfp'], description="Returns a user's avatar", usage="`ft!avatar`")
    async def avatar(self, ctx: Context, *, member: discord.Member = None):
        if member == None:
            member = ctx.author
        
        if member.avatar is None:
            memberAv = member.default_avatar.url
        else:
            memberAv = member.avatar.url

        embed = discord.Embed(title=f"{member.name}'s Avatar", color=color)
        embed.set_image(url=memberAv)
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)
    
    @commands.command(aliases=['serverstats', 'server', 'serverinf', 'servinf'], description="Returns information about the server", usage="`ft!serverinfo`")
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

        await ctx.send(f"This is the Server Information ↗ {ctx.author.mention}!", embed=embed)
    

    @commands.command(description="Returns information about a user", usage="`ft!userinfo`")
    async def userinfo(self, ctx:Context, *, member: discord.Member = None):
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
        # perm_list = discord.Permissions()
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
    
    @commands.command()
    @commands.has_any_role("Owner", "Bot Developer")
    async def rules(self, ctx: Context):
        embed = discord.Embed(
            color = discord.Color.red(),
            title = "Rules",
            description = "Please follow these rules to potentially avoid a warn, mute or ban.",
            timestamp = datetime.datetime.now()
        )
        embed.add_field(
            name = "Be respectful to other users and their privacy.",
            value = "You must make sure you create a safe environment for others.",
            inline = False
        ).add_field(
            name = "Do not post any NSFW content.",
            value = "NSFW is not tolerated at all. You will receive an immediate ban for this action.",
            inline = False
        ).add_field(
            name = "Do not spam.",
            value = "Pretty self-explanatory, right?",
            inline = False
        ).add_field(
            name = "Keep bot commands in their specified channel",
            value = "<#942179597112475687> is there for a reason. Use it.",
            inline = False
        ).add_field(
            name = "English only.",
            value = "Please use English when talking in the chatrooms, it makes moderating easier and makes it easier for other people to understand you (as they are more likely to already know English).",
            inline = False
        ).add_field(
            name = "Swearing is allowed, but with exceptions.",
            value = "Swearing is fine for general conversation, however, we will not tolerate any insults or ways of using swearing in a negative way.",
            inline = False
        ).add_field(
            name = "Use common sense.",
            value = "Just because there might not be a rule listed here, doesn't give you the right to carry out any actions that may cause others to feel unsafe, hurt the server etc.",
            inline = False
        ).set_image(
            url = "attachment://rules.png"
        )
        embed.set_footer(
            text = "Please note that these rules may change anytime.",
            icon_url = self.bot.user.avatar
        )

        await ctx.send(embed = embed, file = discord.File("assets/rules.png"))

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        msg_cnt = message.content.lower()
        if msg_cnt.__contains__("sexo"):
            embed = discord.Embed(color=discord.Color.yellow())
            embed.add_field(
                name = "\n\n\nSexo",
                value = "- Bedezu",
                inline = False
            )
            embed.set_thumbnail(url="https://cdn.shopify.com/s/files/1/1061/1924/products/Flushed_Emoji_Icon_5e6ce936-4add-472b-96ba-9082998adcf7_grande.png?width=473&height=473")
            embed.set_footer(
                text = f"Requested by {message.author} | 😳"
            )
            embed.timestamp = datetime.datetime.now()
            await message.reply(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Miscellaneous(bot))