import sqlite3 as sl
import discord
from discord.ext import commands
from loguru import logger
import discord.ui
class Buttons(discord.ui.View):
    def __init__(self, *, timeout = None):
        super().__init__(timeout=timeout)

    @discord.ui.button(label="+1",style=discord.ButtonStyle.green)
    async def gray_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        pass
class privatevoices(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        try:
            con = sl.connect('voices_private.db')
            cursor = con.cursor()
        except:
            logger.critical("Ошибка инициализации private_voices.db")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS channels (
            channelid INT,
            userid INT
        )""")
        con.commit()
        print("voice channels are ready")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        category_id = 971836593130307664
        make_channel_id = 1071801182596636703
        con = sl.connect('voices_private.db')
        cursor = con.cursor()
        if after.channel:
            if after.channel.id == make_channel_id:
                guild = member.guild

                category = discord.utils.get(guild.categories, id=category_id)

                created_channel = await guild.create_voice_channel(
                    f'┊• {member.display_name} •',
                    position=5,
                    category=category,
                    bitrate=96000
                )

                await created_channel.set_permissions(member, connect=True, mute_members=True, move_members=True, manage_channels=True)
                cursor.execute("INSERT INTO channels VALUES (?, ?)", (created_channel.id, member.id))
                con.commit()
                await member.move_to(created_channel)

        elif before.channel:
            cursor.execute("SELECT channelid FROM channels")
            if cursor.fetchone() is not None:
                if not before.channel.members:
                    cursor.execute(f"DELETE FROM channels WHERE channelid = '{before.channel.id}'")
                    con.commit()
                    return await before.channel.delete()
async def setup(bot):
    await bot.add_cog(privatevoices(bot))
