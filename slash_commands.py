import discord
from discord import app_commands
from discord.ext import commands
import sys
sys.path.append("./Cogs")
import locale
locale.setlocale(locale.LC_ALL, '')
intents = discord.Intents.all()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)
class slash_commands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()
    @commands.Cog.listener()
    async def on_ready(self):
        print("slash_commands are ready to use")
    @app_commands.command(name = 'ping')
    async def _ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'{round(self.bot.latency * 1000)}ms')
class slash_commands_bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=".", intents=discord.Intents.all())
    async def setup_hook(self) -> None:
        await self.tree.copy_global_to(discord.Object(id=842110386215321650))
        await self.tree.sync()
bot = slash_commands_bot()
async def setup(bot):
    await bot.add_cog(slash_commands(bot))