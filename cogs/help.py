import discord, datetime

from discord.ext import commands
from discord import ApplicationContext as Context
from discord import Option

class HelpCog(commands.Cog, name="Help"):
    '''The cog containing the help command'''
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description = "Get help!")
    async def help(self, ctx: Context): #TEMP NAME :pp
        def return_command_embed(cmd: discord.ApplicationCommand):
            try:
                fcmd = self.bot.get_application_command(name = cmd, type = discord.SlashCommand)
            except Exception as e:
                return discord.Embed(
                    title = "Error",
                    description = f"An exception was thrown!\n\nDetails:\n{e}",
                    color = discord.Color.dark_red()
                )
            info = fcmd.to_dict()
            description = info["description"]
            options = info["options"]
            list_op = list()
            final_string = "\n\n"
            if len(options) == 0:
                final_string = "No options"
            else:
                i = 0
                while i + 1 <= len(options):
                    option = options[i]   
                    name = option["name"]
                    desc = option["description"]
                    req = option["required"]
                    choices = option["choices"] if len(option["choices"]) != 0 else "No choices"
                    list_op.append(f"{i + 1}) __Name__: {name}\n* __Description__: {desc}\n * __Required__: {req}\n * __Choices__: {choices}")
                    i += 1
                final_string = "\n\n".join(list_op)
            embed = discord.Embed(
                color = 0xead1dc,
                title = "Command",
                description = f"Here's some info about `{fcmd.name}` command:",
                timestamp = datetime.datetime.now()
            )
            embed.add_field(
                name = "Description",
                value = f"{description}",
                inline = False
            )
            embed.add_field(
                name = "Options",
                value = f"{final_string}",
                inline = False
            )
            embed.set_footer(
                text = "If you have any questions, please contact any staff member!"
            )
            return embed

        async def interaction_check(interaction: discord.Interaction):
            return interaction.user.id == ctx.author.id
        
        async def cbutton_callback(interaction: discord.Interaction):
            embed = discord.Embed(
                description = "Closing in 3 seconds...",
                color = discord.Color.teal()
            )
            msg = await interaction.message.edit(view = None, embed = embed)
            await msg.delete(delay = 3, reason = "User interaction")
        
        cbutton = discord.ui.Button(
            style = discord.ButtonStyle.danger,
            label = "Close",
            emoji = "❌"
            )
        cbutton.callback = cbutton_callback

        # if command == None:
        async def return_commands(bot: commands.Bot):
            async def predict(cmd: commands.Command):
                try:
                    return await cmd.can_run(ctx)
                except commands.CommandError:
                    return False
            options = list()
            for cmd in bot.application_commands:
                if await predict(cmd) == True:
                    options.append(discord.SelectOption(
                        label = cmd.name,
                        emoji = "📜"
                    ))
                else:
                    continue
            return options
            
        async def select_callback(interaction: discord.Interaction):
            await interaction.response.edit_message(content = None, embed = return_command_embed(select.values[0]))

        select = discord.ui.Select(
            placeholder = "Select a command!",
            min_values = 1,
            max_values = 1,
            options = await return_commands(self.bot)
        )
        select.callback = select_callback

        view = discord.ui.View()
        view.add_item(select)
        view.add_item(cbutton)
        view.interaction_check = interaction_check

        embed = discord.Embed(
            description = "Choose the command you want to get info about from the menu below!",
            color = discord.Color.teal()
        )

        await ctx.respond(embed = embed, view = view)

def setup(bot: commands.Bot):
    bot.add_cog(HelpCog(bot))