import nextcord, datetime
from nextcord.ext import commands
from nextcord.ext.commands import Context

welcome_channel_id = 942179597112475681
year = datetime.date.today().year
color = 0xffd500

class Welcoming(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member: nextcord.Member):
        embed = nextcord.Embed(title="Aww Man!", 
            description=f"👋 {member.mention} Has Left the Server!\nWe hope you have had a great time here! :D", 
            color=color
        )
        embed.set_thumbnail(url=member.avatar.url)
        await member.guild.get_channel(welcome_channel_id).send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        embed = nextcord.Embed(title="Heyo there!", 
            description=f"👋 {member.mention} Welcome to the Server!\nWe hope you have a great time here :D", 
            color=color
        )
        embed.set_thumbnail(url=member.avatar.url)
        await member.guild.get_channel(welcome_channel_id).send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Welcoming(bot))
