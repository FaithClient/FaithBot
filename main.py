import nextcord, os

from nextcord.ext import commands
from dotenv import load_dotenv

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

@client.command()
async def ping(interaction):
    await interaction.send(f"Current Ping is {round(client.latency * 1000)}ms")

if __name__ == "__main__":
    load_dotenv()
    client.run(os.getenv("DISCORD_TOKEN"))