import discord, datetime

from discord.ext import commands
from discord import ApplicationContext as Context
from discord import Option

class HelpCog(commands.Cog, name="Help"):
    '''The cog containing the help command'''
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    # @commands.slash_command(description="Returns the help embed")
    # async def help(self, ctx: Context, cmd: Option(str, name = "command", description = "idk testing ig", required = False), cogg: Option(str, name = "cog", description = "Testing again", required = False)):
    #     '''Returns the help embed'''
    #     async def predict(cmd: commands.Command):
    #         try:
    #             return await cmd.can_run(ctx)
    #         except commands.CommandError:
    #             return False
    #     if cmd == None and cogg == None:
    #         embed = discord.Embed(color=discord.Color.teal())
    #         for cog_name, cog in self.bot.cogs.items():
    #             overall = []
    #             exec_cmds = [cmd for cmd in cog.get_commands() if await predict(cmd) == True]
    #             for com in cog.get_commands():
    #                 if com in exec_cmds:
    #                     overall.append(com)
    #             if len(overall) == 0:
    #                 continue
    #             cmds = [f"`{cmd.name}`" for cmd in overall]
    #             final = ", ".join(cmds)
    #             embed.add_field(
    #                 name = cog.qualified_name if cog else "No category",
    #                 value = final,
    #                 inline = False
    #             )
    #         embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar)
    #         embed.timestamp = datetime.datetime.now()
    #         await ctx.respond(embed=embed)
    #     elif cmd == None and cogg != None and cog in self.bot.cogs:
    #         cog = self.bot.get_cog(cogg)
    #         exec_cmds = []
    #         for cmd in cog.get_commands():
    #             if await predict(cmd) == True:
    #                 exec_cmds.append(f"`{cmd.name}`")
    #         if len(exec_cmds) == 0:
    #             embed = discord.Embed(
    #                 title = "Error", 
    #                 description = "You do not have permission to view this cog",
    #                 color = discord.Color.dark_teal())
    #             embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar)
    #             embed.timestamp = datetime.datetime.now()
    #             await ctx.respond(embed=embed)
    #         elif len(exec_cmds) > 0:
    #             embed = discord.Embed(title=cog.qualified_name, color=discord.Color.teal())
    #             embed.add_field(
    #                 name = "Commands",
    #                 value = ", ".join(exec_cmds),
    #                 inline = False
    #             )
    #             embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar)
    #             embed.timestamp = datetime.datetime.now()
    #             await ctx.respond(embed=embed)
    #     elif cmd != None and cog == None and self.bot.get_command(cmd) in self.bot.commands:
    #         cmd = self.bot.get_command(cmd)
    #         if await predict(cmd) == True:
    #             embed = discord.Embed(title="Command Info 📜", color=discord.Color.teal())
    #             embed.add_field(
    #                 name = "Command Name",
    #                 value = cmd.name,
    #                 inline = True
    #             )
    #             embed.add_field(
    #                 name = "Command Description",
    #                 value = cmd.description if cmd.description is not None else "Not set",
    #                 inline = True
    #             )
    #             embed.add_field(
    #                 name = "Command Cog",
    #                 value = f"{cmd.cog_name}" if cmd.cog_name is not None else "No category",
    #                 inline = True
    #             )
    #             al = []
    #             for alias in cmd.aliases:
    #                 al.append(f"`{alias}`")
    #             if len(al) == 1:
    #                 embed.add_field(
    #                     name = "Command Aliases",
    #                     value = " ".join(al),
    #                     inline = True
    #                 )
    #             else:
    #                 embed.add_field(
    #                     name = "Command Aliases",
    #                     value = ", ".join(al) if len(al) != 0 else "None",
    #                     inline = True
    #                 )
    #             embed.add_field(
    #                 name = "Command Usage",
    #                 value = cmd.usage if cmd.usage is not None else "Not set",
    #                 inline = True
    #             )
    #             embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar)
    #             embed.timestamp = datetime.datetime.now()
    #             await ctx.respond(embed=embed)
    #         elif cmd != None and cogg != None:
    #             await ctx.respond("OOP ERROR BOY")
    #         else:
    #             embed = discord.Embed(
    #                 title = "Error", 
    #                 description = "You do not have permission to view this command",
    #                 color = discord.Color.dark_teal())
    #             embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar)
    #             embed.timestamp = datetime.datetime.now()
    #             await ctx.respond(embed=embed)
    #     else:
    #         embed = discord.Embed(
    #             title = "Error", 
    #             description = f"**Invalid** command/cog...\nType `{self.bot.command_prefix}help` for a complete list of the accessible to you commands/cogs.",
    #             color = discord.Color.dark_teal())
    #         embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar)
    #         embed.timestamp = datetime.datetime.now()
    #         await ctx.respond(embed=embed)

    @commands.slash_command(description = "Get help!")
    @discord.commands.option(name = "command", type = str, description = "Testing 1", required = False)
    @discord.commands.option(name = "cog", type = str, description = "Testing 2", required = False)
    async def new_help(self, ctx: Context, command: str, cog: str): #TEMP NAME :pp
        if command == None and cog == None:
            
            def return_commands(bot: commands.Bot):
                options = list()
                for cmd in bot.application_commands:
                    options.append(discord.SelectOption(
                        label = cmd.name,
                        emoji = "📜"
                    ))
                return options
            
            async def select_callback(interaction: discord.Interaction):
                await interaction.response.send_message(f"You selected {select.values[0]}")
            
            async def interaction_check(interaction: discord.Interaction):
                return interaction.user.id == ctx.author.id

            select = discord.ui.Select(
                placeholder = "Select a command!",
                min_values = 1,
                max_values = 1,
                options = return_commands(self.bot)
            )

            select.callback = select_callback

            view = discord.ui.View()
            view.add_item(select)
            view.interaction_check = interaction_check

            await ctx.respond(content = "Ayo, wait a minute...", view = view)

def setup(bot: commands.Bot):
    bot.add_cog(HelpCog(bot))