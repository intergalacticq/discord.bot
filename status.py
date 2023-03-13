import sqlite3 as sl
import discord
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
class status(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.status =cycle('Watching Aneko','Wathing You'])
    @tasks.loop(seconds=5.0)
    async def change_status(self):
        await self.bot.change_presence(activity=discord.Game(next(self.status)))
    @commands.Cog.listener()
    async def on_ready(self):
        print("status change is ready")
        self.change_status.start()
async def setup(bot):
    await bot.add_cog(status(bot))
