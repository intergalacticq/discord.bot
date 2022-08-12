import locale
locale.setlocale(locale.LC_ALL, '')
import random
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("token")
import asyncio
import discord
from tkinter import COMMAND
intents = discord.Intents.default()
intents.members = True
client = discord.Client()
from discord.ext import commands
client = commands.Bot(command_prefix="!", intents=intents)
from discord import utils
from discord import user
from discord import message
from discord import guild
import config
from discord.utils import get
from discord import member
rnd = random.SystemRandom()

@client.event
async def on_member_join(member):
    global b
    b = random.randint(1000, 9000)
    channel = client.get_channel(847951541621358652)
    embedVar = discord.Embed(title="══════════════:rocket: Aneko ══════════════", description="**Добро пожаловать в галактику Aneko**", color=0xff2ede)
    embedVar.add_field(name="Обязательно прочитайте правила, их не знание не освобождает от ответственности!", value="В нашей галактике ты найдёшь: новые знакомства, активное общение, экономика, множество ролей для украшения вашего профиля, адекватная и отзывчивая модерация всегда готова помочь.Соблюдайте правила и наслаждайтесь атмосферой!", inline=False)
    embedVar.add_field(name="Чтобы попасть к нам, вам следует пройти проверку!", value="отправь код, который прислал бот, по примеру: !1234(у тебя есть 10 минут, чтобы отправить код, иначе, он пропадет)", inline=False)
    embedVar.set_image(url="https://cdn.discordapp.com/attachments/860220993137803264/909856106304663552/3.jpg")
    await channel.send(embed=embedVar, delete_after= 600)
    await channel.send(f'{member.mention}, перед цифрами ставь ! ',delete_after= 600)
    await channel.send(b, delete_after= 600)
@client.event
async def on_message(message):
    verify_channel = client.get_channel(847951541621358652)
    all_channel = client.get_channel(845009437261037678)
    verify_role = discord.utils.get(message.guild.roles, name='╬ㅤㅤ🔎Искательㅤㅤㅤ╬')
    if message.content == ('!' + str(b)) and message.channel == verify_channel:
        member = message.author
        await member.add_roles(verify_role)
        await message.delete(delay = 600)
        await all_channel.send(f'{member.mention}, приветик, добро пожаловать в нашу галактику!\n Обязательно ознакомься с <#842300946537119784> и <#842301178398375936>.\n Приятного общения!')
    elif message.content != ('!' + str(b)) and message.channel == verify_channel:
        await message.delete(delay = 600)
    elif message.content != ('!' + str(b)) and message.channel != verify_channel:
        pass
@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 1003651093206663210 and payload.emoji.name == "✅":
            print('got message and reaction on it')
            guild = discord.utils.get(client.guilds, id=payload.guild_id)
            print('got guild')
            role = discord.utils.get(guild.roles, name='╬ㅤㅤㅤヾ(≧▽≦*)oㅤㅤㅤ╬')
            print('got the role')
            await payload.member.add_roles(role)
            print('gave the role to member')
@client.event
async def on_raw_reaction_remove(payload):
    guild = client.get_guild(payload.guild_id)
    print("Guild checked.")
    member = discord.utils.get(guild.members, id=payload.user_id)
    print("Member checked.")
    if payload.message_id == 1003651093206663210:
        print("Got message.")
        if str(payload.emoji) == "✅":
            print("Checked for the reaction.")
            role = discord.utils.get(guild.roles, name='╬ㅤㅤㅤヾ(≧▽≦*)oㅤㅤㅤ╬')
            print("Got the role.")
        if role is not None:
            role = discord.utils.get(guild.roles, name='╬ㅤㅤㅤヾ(≧▽≦*)oㅤㅤㅤ╬')
            await member.remove_roles(role, reason = None)
            print("Removed the role")

client.run(token)