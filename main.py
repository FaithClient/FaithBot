import nextcord, os
import datetime

from nextcord.ext import commands
from dotenv import load_dotenv

welcome_channel_id = 942179597112475681
year = datetime.date.today().year
# intents = nextcord.Intents.default()
# intents.members = True #DEV ENABLE ALL OF THE INTENTS!!!!!!!
client = commands.Bot(command_prefix='f!', status=nextcord.Status.idle)

@client.event
async def on_ready():
    print(f"successfully logged in as {client.user}")
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="FaithClient Users!"))

@client.event
async def on_member_join(member: nextcord.Member):
    embed = nextcord.Embed(description=f"👋 {member.mention} Welcome to the server!", color=nextcord.Color.blurple())
    embed.set_thumbnail(url=member.avatar)
    await member.guild.get_channel(welcome_channel_id).send(embed=embed)


@client.command()
async def ping(interaction):
    footer = f"Requested by {interaction.user}"
    embed = nextcord.Embed(
        color=0x5539cc,
        title="Ping Pong! 🏓",
        
    )
    embed.add_field(name='Bot Latency!', value=f"Bot Ping is **{round(client.latency * 1000)}ms**", inline=True)
    embed.set_author(name=client.user, icon_url=client.user.avatar)
    embed.set_footer(text=footer)
    embed.set_thumbnail(url=client.user.avatar)
    embed.timestamp = datetime.datetime.utcnow()
    await interaction.send(embed=embed)

if __name__ == "__main__":
    load_dotenv()
    client.run(os.getenv("DISCORD_TOKEN"))