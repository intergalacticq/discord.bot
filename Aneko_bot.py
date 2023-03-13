import discord
import locale
locale.setlocale(locale.LC_ALL, '')
from discord.ext import commands
from loguru import logger
import os
import asyncio
from discord.ext import tasks, commands
TOKEN = 'OTUxMDUxMzA5NzY5OTc3ODk4.GkH66A.OX34IAEG8d_rXTrQl4sNWpawc2wJpWgaKsJvHs'
bot = commands.Bot(command_prefix= ".", intents=discord.Intents.all())
bot.remove_command( "help" )
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
            except:
                logger.error(f"Error loading extension {filename[:-3]}")
            finally:    
                logger.info(f"loaded extension {filename[:-3]}")
async def main():
    async with bot:
        @bot.event
        async def on_ready(): 
            logger.info("Fudzinami ready and loves u")
        await load_extensions()
        await bot.start(TOKEN)
asyncio.run(main())