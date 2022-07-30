import nextcord, datetime

from nextcord.ext import commands
from nextcord.ext.commands import Context

class HelpCog(commands.Cog, name="Help"):
    '''The cog containing the help command'''
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(description="Returns the help embed", usage="`ft!help`\n`ft!help <cog>`\n`ft!help <command>`")
    async def help(self, ctx: Context, param = None):
        '''Returns the help embed'''
        async def predict(cmd: commands.Command):
            try:
                return await cmd.can_run(ctx)
            except commands.CommandError:
                return False
        if param == None:
            embed = nextcord.Embed(color=nextcord.Color.teal(), description=f"Type `{self.bot.command_prefix}help <cog>` to learn more about a cog\nType `{self.bot.command_prefix}help <command>` to learn more about a specific command")
            for cog_name, cog in self.bot.cogs.items():
                overall = []
                exec_cmds = [cmd for cmd in cog.get_commands() if await predict(cmd) == True]
                for com in cog.get_commands():
                    if com in exec_cmds:
                        overall.append(com)
                if len(overall) == 0:
                    continue
                cmds = [f"`{cmd.name}`" for cmd in overall]
                final = ", ".join(cmds)
                embed.add_field(
                    name = cog.qualified_name if cog else "No category",
                    value = final,
                    inline = False
                )
            embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        elif param in self.bot.cogs:
            cog = self.bot.get_cog(param)
            exec_cmds = []
            for cmd in cog.get_commands():
                if await predict(cmd) == True:
                    exec_cmds.append(f"`{cmd.name}`")
            if len(exec_cmds) == 0:
                embed = nextcord.Embed(
                    title = "Error", 
                    description = "You do not have permission to view this cog",
                    color = nextcord.Color.dark_teal())
                embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar)
                embed.timestamp = datetime.datetime.now()
                await ctx.send(embed=embed)
            elif len(exec_cmds) > 0:
                embed = nextcord.Embed(title=cog.qualified_name, color=nextcord.Color.teal())
                embed.add_field(
                    name = "Commands",
                    value = ", ".join(exec_cmds),
                    inline = False
                )
                embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar)
                embed.timestamp = datetime.datetime.now()
                await ctx.send(embed=embed)
        elif self.bot.get_command(param) in self.bot.commands:
            cmd = self.bot.get_command(param)
            if await predict(cmd) == True:
                embed = nextcord.Embed(title="Command Info 📜", color=nextcord.Color.teal())
                embed.add_field(
                    name = "Command Name",
                    value = cmd.name,
                    inline = True
                )
                embed.add_field(
                    name = "Command Description",
                    value = cmd.description if cmd.description is not None else "Not set",
                    inline = True
                )
                embed.add_field(
                    name = "Command Cog",
                    value = f"{cmd.cog_name}" if cmd.cog_name is not None else "No category",
                    inline = True
                )
                al = []
                for alias in cmd.aliases:
                    al.append(f"`{alias}`")
                if len(al) == 1:
                    embed.add_field(
                        name = "Command Aliases",
                        value = " ".join(al),
                        inline = True
                    )
                else:
                    embed.add_field(
                        name = "Command Aliases",
                        value = ", ".join(al) if len(al) != 0 else "None",
                        inline = True
                    )
                embed.add_field(
                    name = "Command Usage",
                    value = cmd.usage if cmd.usage is not None else "Not set",
                    inline = True
                )
                embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar)
                embed.timestamp = datetime.datetime.now()
                await ctx.send(embed=embed)
            else:
                embed = nextcord.Embed(
                    title = "Error", 
                    description = "You do not have permission to view this command",
                    color = nextcord.Color.dark_teal())
                embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar)
                embed.timestamp = datetime.datetime.now()
                await ctx.send(embed=embed)
        else:
            embed = nextcord.Embed(
                title = "Error", 
                description = f"**Invalid** command/cog...\nType `{self.bot.command_prefix}help` for a complete list of the accessible to you commands/cogs.",
                color = nextcord.Color.dark_teal())
            embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(HelpCog(bot))