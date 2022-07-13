import nextcord, datetime, humanfriendly

from nextcord.ext import commands
from nextcord.ext.commands import Context

year = datetime.date.today().year
color = 0xffd500

class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    #@commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: nextcord.Member, *, reason=None):
        if member == ctx.guild.owner:
            await ctx.send(f"You can't kick the owner! {ctx.author.mention}")
            return
        if member.guild_permissions.administrator:
            await ctx.send(f"YOU CANT KICK AN ADMIN! {ctx.author.mention}")
            return
        if member == ctx.author:
            await ctx.send(f"You can't kick yourself {member.mention}")
            return

        await member.kick(reason=reason)
        embed1 = nextcord.Embed(title=f'{member.name}#{member.discriminator} has been kicked!',color=color)
        embed2 = nextcord.Embed(title=f'{member.name}#{member.discriminator} has been kicked!',color=color)

        if reason == None:
            embed1.add_field(name='User Kicked',value=f'User: {member.mention}', inline=False)
            embed1.set_footer(text=f'Requested by {ctx.author.mention}')
            embed1.timestamp = datetime.datetime.now()

            await ctx.send(embed=embed1)
        else:
            embed2.add_field(name='User Kicked',value=f'User: {member.mention}', inline=False)
            embed2.add_field(name='Reason for Kick',value=f'Reason: {reason}', inline=False)
            embed2.set_footer(text=f'Requested by {ctx.author}')
            embed2.timestamp = datetime.datetime.now()

            await ctx.send(embed=embed2)
    
    @commands.command()
    async def mute(self, ctx, member: nextcord.Member, time, *, reason):
        time = humanfriendly.parse_timespan(time)
        if member == ctx.guild.owner:
            await ctx.send(f"You can't mute the owner! {ctx.author.mention}")
            return
        if member.guild_permissions.administrator:
            await ctx.send(f"YOU CANT MUTE AN ADMIN! {ctx.author.mention}")
            return
        if member == ctx.author:
            await ctx.send(f"You can't mute yourself {member.mention}")
            return
        
        await member.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=time))

        embedTime = nextcord.Embed(title=f'{ctx.author} has muted a member!', color=color)
        embedTime.add_field(name='User Muted', value=f'User: {member.mention}', inline=False)
        embedTime.add_field(name='Reason for Mute', value=f'Reason: {reason}', inline=False)
        embedTime.set_footer(text=f'Requested by {ctx.author}')
        embedTime.timestamp = datetime.datetime.now()

        await ctx.send(embed=embedTime)

    @commands.command()
    async def unmute(self, ctx: Context, member: nextcord.Member, *, reason):
        if member._timeout is None:
            await ctx.reply(f"Member does not have an active Timeout! {ctx.author.mention}")
            return
        else:
            await member.edit(timeout=None)

        embedTime = nextcord.Embed(title=f'{ctx.author} has unmuted a member!', color=color)
        embedTime.add_field(name='User Unmuted', value=f'User: {member.mention}', inline=False)
        embedTime.add_field(name='Reason for Unmute', value=f'Reason: {reason}', inline=False)
        embedTime.set_footer(text=f'Requested by {ctx.author}')
        embedTime.timestamp = datetime.datetime.now()

        await ctx.send(embed=embedTime)

def setup(bot: commands.Bot):
    bot.add_cog(Moderation(bot))