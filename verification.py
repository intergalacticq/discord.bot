import discord
import locale
locale.setlocale(locale.LC_ALL, '')
import random
from discord.ext import commands
rnd = random.SystemRandom()
intents = discord.Intents.all()
intents.members = True
bot = discord.Client(intents=intents)
from discord.ext import commands
from discord import app_commands
global b
b = 0
class verification(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Verification ready")        
    @commands.Cog.listener()
    async def on_member_join(self,member):
        global b
        b = random.randint(1000,9999)
        channel = discord.utils.get(member.guild.channels, id = 847951541621358652)
        embedVar = discord.Embed(title="══════════════:rocket: Aneko ══════════════", description="**Добро пожаловать в галактику Aneko**", color=0xff2ede)
        embedVar.add_field(name="Обязательно прочитайте правила, их не знание не освобождает от ответственности!", value="В нашей галактике ты найдёшь: новые знакомства, активное общение, экономика, множество ролей для украшения вашего профиля. Соблюдайте правила и наслаждайтесь атмосферой!", inline=False)
        embedVar.add_field(name="Чтобы попасть к нам, вам следует пройти проверку!", value="отправь код, который прислал бот, по примеру: !1234 (у тебя есть 10 минут, чтобы отправить код, иначе, он пропадет)", inline=False)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/860220993137803264/909856106304663552/3.jpg")
        await channel.send(embed=embedVar, delete_after= 601)
        await channel.send(f'{member.mention}, привет, **ПЕРЕД** цифрами ставь **!**\n**Пример: !1234**\n**ТОЛЬКО ЭТОТ** код действует для **ВСЕХ** в чате ↓(предыдущий не работает)\n'+'!'+str(b),delete_after= 602)     
    @app_commands.command(name = 'code')
    async def _code(self, interaction: discord.Interaction):
        await interaction.response.send_message("Введи !" + str(b))    
    @commands.Cog.listener()
    async def on_message(self,message):
        dv_channel = self.bot.get_channel(1075421565606432808)
        guild = self.bot.get_guild(842110386215321650)
        verify_channel = self.bot.get_channel(847951541621358652)
        all_channel = self.bot.get_channel(845009437261037678)
        verify_role = discord.utils.get(guild.roles, id=847805867247534101)
        if ((message.content == ('!' + str(b)) or message.content == ('! ' + str(b))) and message.channel == verify_channel):
            member = message.author
            await member.add_roles(verify_role)
            await message.delete(delay = 606)   
            await all_channel.send(f'┌ Приветик {member.mention}, добро пожаловать в нашу галактику!<a:rockeet:879453830805356626>\n├ Обязательно ознакомься с <#842300946537119784> и <#842301178398375936><a:moon_stars:938034916392828928> .\n├ Также можешь взять <#842710136307843072>.<a:love_planet:938034915876954142> \n└ Приятного общения!<a:Aneko:880196029448867911>\n||<@&842153877377515540>,<@&953259625090781186>,<@&842326868811710484>||',delete_after= 610)
            await dv_channel.send(f'{member.mention} Зашёл на сервер! Не забывайте о нём!')
            try:
                await member.send(f'Приветик, мой сладкий пирожочек!<a:heart_s:879453830192959488>.Добро пожаловать в прекрасную галактику! Наш сервер **строго** 13+. \nНе забудь прочитать наши <#842300946537119784>. Любые ваши предупреждение от администраторов вы можете оспорить с `INTERGALAXY#4607`<a:cat_watermelon:880196029784399903> \nПриятного времяпрепровождения!<a:paw_red:938034915629465621>|| Ссылка для приглашения друга -> https://discord.gg/B5npfBWqUu||')
            except:
                print("member has closed DM, CAN'T SEND MESSAGE TO {member.display_name}")
        elif message.content != ('!' + str(b)) and message.channel == verify_channel:
            await message.delete(delay = 607)
        elif message.content == ('!' + str(b)) and message.channel != verify_channel:
            pass
        message_channel = bot.get_channel(1042157113620840599)
        send_message_channel = bot.get_channel(845009437261037678)
        if message.channel == message_channel  and message.author.id == 323895676515909632:
            await send_message_channel.send(message.content)
        reaction_channel = bot.get_channel(853548086000877598)
        if message.channel == reaction_channel:
            await message.add_reaction(':1_:880196029587259462')
            await message.add_reaction(':1_:880196029138472991')
async def setup(bot):
    await bot.add_cog(verification(bot))

