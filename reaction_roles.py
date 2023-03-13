import discord
from discord.ext import commands
intents = discord.Intents.all()
intents.members = True
bot = discord.Client(intents=intents)
global guild
class reaction_roles(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        global guild
        guild = self.bot.get_guild(842110386215321650)
        print(f"ReactionRoles ready.")        
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        global guild
#навигация
        if payload.message_id == 1008010227276329020 and payload.emoji.name == "🎄":
            role = discord.utils.get(guild.roles, id=849026949825036328)
            await payload.member.add_roles(role, reason="navigaciya", atomic=True)
        if payload.message_id == 1008010227276329020 and payload.emoji.name == "🔑":
            role = discord.utils.get(guild.roles, id=903217039387279360)
            await payload.member.add_roles(role, reason="navigaciya", atomic=True)
        if payload.message_id == 1008010227276329020 and payload.emoji.name == "🥞":
            role = discord.utils.get(guild.roles, id=883990209325326377)
            await payload.member.add_roles(role, reason="navigaciya", atomic=True)
#роли
     #рофл 
        if payload.message_id == 943518613229412362 and payload.emoji.name == "🎸":
            role = discord.utils.get(guild.roles, id=847543592264138773)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518613229412362 and payload.emoji.name == "🍷":
            role = discord.utils.get(guild.roles, id=847558165830696980)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518613229412362 and payload.emoji.name == "🍺":
            role = discord.utils.get(guild.roles, id=847558166413443092)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518613229412362 and payload.emoji.name == "🥏":
            role = discord.utils.get(guild.roles, id=847543593371566147)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518613229412362 and payload.emoji.name == "🤘":
            role = discord.utils.get(guild.roles, id =847558165247164436)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518613229412362 and payload.emoji.name == "💉":
            role = discord.utils.get(guild.roles, id=847558166518693949)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518613229412362 and payload.emoji.name == "🗿":
            role = discord.utils.get(guild.roles, id=847558163922026546)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518613229412362 and payload.emoji.name == "🧵":
            role = discord.utils.get(guild.roles, id=847558164752236554)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518613229412362 and payload.emoji.name == "🚫":
            role = discord.utils.get(guild.roles, id=847558163431161957)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518613229412362 and payload.emoji.name == "💀":
            role = discord.utils.get(guild.roles, id=847543591970144306)
            await payload.member.add_roles(role, reason="roli", atomic=True)
         #гендер-возраст
        if payload.message_id == 943518614647095296 and payload.emoji.name == "♂":
            role = discord.utils.get(guild.roles, id=847805864966619146)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518614647095296 and payload.emoji.name == "♀":
            role = discord.utils.get(guild.roles, id=847805866300276776)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518614647095296 and payload.emoji.name == "🤡":
            role = discord.utils.get(guild.roles, id=864880760011882537)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518614647095296 and payload.emoji.name == "1️⃣":
            role = discord.utils.get(guild.roles, id=868871541864165396)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518614647095296 and payload.emoji.name == "2️⃣":
            role = discord.utils.get(guild.roles, id=868871544775012433)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518614647095296 and payload.emoji.name == "3️⃣":
            role = discord.utils.get(guild.roles, id=868871543042748417)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518614647095296 and payload.emoji.name == "4️⃣":
            role = discord.utils.get(guild.roles, id=878158148584747028)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        #занятия
        if payload.message_id == 943518616127701072 and payload.emoji.name == "🎷":
            role = discord.utils.get(guild.roles, id=849026950772293662)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518616127701072 and payload.emoji.name == "📷":
            role = discord.utils.get(guild.roles, id=849026947823566869)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518616127701072 and payload.emoji.name == "🌲":
            role = discord.utils.get(guild.roles, id=849026949825036328)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518616127701072 and payload.emoji.name == "🏋":
            role = discord.utils.get(guild.roles, id=880128611733082112)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518616127701072 and payload.emoji.name == "🦋":
            role = discord.utils.get(guild.roles, id=880128612253179934)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518616127701072 and payload.emoji.name == "🎭":
            role = discord.utils.get(guild.roles, id=880128612894920725)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518616127701072 and payload.emoji.name == "🎨":
            role = discord.utils.get(guild.roles, id=849024409091702826)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518616127701072 and payload.emoji.name == "🎙":
            role = discord.utils.get(guild.roles, id=878160955522039818)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518616127701072 and payload.emoji.name == "💻":
            role = discord.utils.get(guild.roles, id=849024411684175942)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518616127701072 and payload.emoji.name == "📝":
            role = discord.utils.get(guild.roles, id=849024407824760872)
            await payload.member.add_roles(role, reason="roli", atomic=True)
    #ИГРЫ
        if payload.message_id == 943518617495023638 and payload.emoji.name == "🔫":
            role = discord.utils.get(guild.roles, id=883990164324618261)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518617495023638 and payload.emoji.name == "⚠️":
            role = discord.utils.get(guild.roles, id=847806043165949982)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518617495023638 and payload.emoji.name == "🔪":
            role = discord.utils.get(guild.roles, id=883990208528404510)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518617495023638 and payload.emoji.name == "🦞":
            role = discord.utils.get(guild.roles, id=849024322181529652)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518617495023638 and payload.emoji.name == "🚗":
            role = discord.utils.get(guild.roles, id=878159071348396052)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518617495023638 and payload.emoji.name == "🔧":
            role = discord.utils.get(guild.roles, id=878166632520880169)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518617495023638 and payload.emoji.name == "🪔":
            role = discord.utils.get(guild.roles, id=853691593277964308)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518617495023638 and payload.emoji.name == "🚔":
            role = discord.utils.get(guild.roles, id=848834740071956490)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518617495023638 and payload.emoji.name == "🦐":
            role = discord.utils.get(guild.roles, id=849024325252022282)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518617495023638 and payload.emoji.name == "🌵":
            role = discord.utils.get(guild.roles, id=849024321401520128)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518617495023638 and payload.emoji.name == "⭕":
            role = discord.utils.get(guild.roles, id=847805865825796116)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518617495023638 and payload.emoji.name == "🦀":
            role = discord.utils.get(guild.roles, id=849024324374757397)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518617495023638 and payload.emoji.name == "💦":
            role = discord.utils.get(guild.roles, id=853691591049740328)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518617495023638 and payload.emoji.name == "🔊":
            role = discord.utils.get(guild.roles, id=848834726051577916)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518617495023638 and payload.emoji.name == "💈":
            role = discord.utils.get(guild.roles, id=853691592443691059)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518617495023638 and payload.emoji.name == "🌊":
            role = discord.utils.get(guild.roles, id=849024324157308928)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518617495023638 and payload.emoji.name == "🌲":
            role = discord.utils.get(guild.roles, id=849026952585150505)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518617495023638 and payload.emoji.name == "⚡":
            role = discord.utils.get(guild.roles, id=847805865256157215)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518617495023638 and payload.emoji.name == "☁️":
            role = discord.utils.get(guild.roles, id=849026952996454470)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518617495023638 and payload.emoji.name == "🧭":
            role = discord.utils.get(guild.roles, id=853691590214942730)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        if payload.message_id == 943518619214676028 and payload.emoji.name == "🌈":
            role = discord.utils.get(guild.roles, id=883990162932113448)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518619214676028 and payload.emoji.name == "🪓":
            role = discord.utils.get(guild.roles, id=883990161296351282)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943518619214676028 and payload.emoji.name == "🧨":
            role = discord.utils.get(guild.roles, id=883990163448021002)
            await payload.member.add_roles(role, reason="roli", atomic=True)
        elif payload.message_id == 943521694914576464 and payload.emoji.name == "🎄":
            role = discord.utils.get(guild.roles, id=849026949825036328)
            await payload.member.add_roles(role)
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
#навигация
        member = discord.utils.get(guild.members, id=payload.user_id)
        if payload.message_id == 1008010227276329020 and str(payload.emoji) == "🎄":
            role = discord.utils.get(guild.roles, id=849026949825036328)
            await member.remove_roles(role)
        elif payload.message_id == 1008010227276329020 and str(payload.emoji) == "🔑":
            role = discord.utils.get(guild.roles, id=903217039387279360)
            await member.remove_roles(role)
        elif payload.message_id == 1008010227276329020 and str(payload.emoji) == "🥞":
            role = discord.utils.get(guild.roles, id=883990209325326377)
            await member.remove_roles(role)
#роли
     #рофл 
        if payload.message_id == 943518613229412362 and str(payload.emoji) == "🎸":
            role = discord.utils.get(guild.roles, id=847543592264138773)
            await member.remove_roles(role)
        elif payload.message_id == 943518613229412362 and str(payload.emoji) == "🍷":
            role = discord.utils.get(guild.roles, id=847558165830696980)
            await member.remove_roles(role)
        elif payload.message_id == 943518613229412362 and str(payload.emoji) == "🍺":
            role = discord.utils.get(guild.roles, id=847558166413443092)
            await member.remove_roles(role)
        elif payload.message_id == 943518613229412362 and str(payload.emoji) == "🥏":
            role = discord.utils.get(guild.roles, id=847543593371566147)
            await member.remove_roles(role)
        elif payload.message_id == 943518613229412362 and str(payload.emoji) == "🤘":
            role = discord.utils.get(guild.roles, id=847558165247164436)
            await member.remove_roles(role)
        elif payload.message_id == 943518613229412362 and str(payload.emoji) == "💉":
            role = discord.utils.get(guild.roles, id=847558166518693949)
            await member.remove_roles(role)
        elif payload.message_id == 943518613229412362 and str(payload.emoji) == "🗿":
            role = discord.utils.get(guild.roles, id=847558163922026546)
            await member.remove_roles(role)
        elif payload.message_id == 943518613229412362 and str(payload.emoji) == "🧵":
            role = discord.utils.get(guild.roles, id=847558164752236554)
            await member.remove_roles(role)
        elif payload.message_id == 943518613229412362 and payload.message_id == 943518613229412362 and str(payload.emoji) == "🚫":
            role = discord.utils.get(guild.roles, id=847558163431161957)
            await member.remove_roles(role)
        elif payload.message_id == 943518613229412362 and str(payload.emoji) == "💀":
            role = discord.utils.get(guild.roles, id=847543591970144306)
            await member.remove_roles(role)
    #гендер-возраст
        if payload.message_id == 943518614647095296 and str(payload.emoji) == "♂":
            role = discord.utils.get(guild.roles, id=847805864966619146)
            await member.remove_roles(role)
        elif payload.message_id == 943518614647095296 and str(payload.emoji) == "♀":
            role = discord.utils.get(guild.roles, id=847805866300276776)
            await member.remove_roles(role)
        elif payload.message_id == 943518614647095296 and str(payload.emoji) == "🤡":
            role = discord.utils.get(guild.roles, id=864880760011882537)
            await member.remove_roles(role)
        elif payload.message_id == 943518614647095296 and str(payload.emoji) == "1️⃣":
            role = discord.utils.get(guild.roles, id=868871541864165396)
            await member.remove_roles(role)
        elif payload.message_id == 943518614647095296 and str(payload.emoji) == "2️⃣":
            role = discord.utils.get(guild.roles, id=868871544775012433)
            await member.remove_roles(role)
        elif payload.message_id == 943518614647095296 and str(payload.emoji) == "3️⃣":
            role = discord.utils.get(guild.roles, id=868871543042748417)
            await member.remove_roles(role)
        elif payload.message_id == 943518614647095296 and str(payload.emoji) == "4️⃣":
            role = discord.utils.get(guild.roles, id=878158148584747028)
            await member.remove_roles(role)
        #занятия
        if payload.message_id == 943518616127701072 and str(payload.emoji) == "🎷":
            role = discord.utils.get(guild.roles, id=849026950772293662)
            await member.remove_roles(role)
        if payload.message_id == 943518616127701072 and str(payload.emoji) == "📷":
            role = discord.utils.get(guild.roles, id=849026947823566869)
            await member.remove_roles(role)
        if payload.message_id == 943518616127701072 and str(payload.emoji) == "🌲":
            role = discord.utils.get(guild.roles, id=849026949825036328)
            await member.remove_roles(role)
        if payload.message_id == 943518616127701072 and str(payload.emoji) == "🏋":
            role = discord.utils.get(guild.roles, id=880128611733082112)
            await member.remove_roles(role)
        if payload.message_id == 943518616127701072 and str(payload.emoji) == "🦋":
            role = discord.utils.get(guild.roles, id=880128612253179934)
            await member.remove_roles(role)
        if payload.message_id == 943518616127701072 and str(payload.emoji) == "🎭":
            role = discord.utils.get(guild.roles, id=880128612894920725)
            await member.remove_roles(role)
        if payload.message_id == 943518616127701072 and str(payload.emoji) == "🎨":
            role = discord.utils.get(guild.roles, id=849024409091702826)
            await member.remove_roles(role)
        if payload.message_id == 943518616127701072 and str(payload.emoji) == "🎙":
            role = discord.utils.get(guild.roles, id=878160955522039818)
            await member.remove_roles(role)
        if payload.message_id == 943518616127701072 and str(payload.emoji) == "💻":
            role = discord.utils.get(guild.roles, id=849024411684175942)
            await member.remove_roles(role)
        if payload.message_id == 943518616127701072 and str(payload.emoji) == "📝":
            role = discord.utils.get(guild.roles, id=849024407824760872)
            await member.remove_roles(role)
            #игры
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "🔫":
            role = discord.utils.get(guild.roles, id=883990164324618261)
            await member.remove_roles(role)
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "⚠️":
            role = discord.utils.get(guild.roles, id=847806043165949982)
            await member.remove_roles(role)
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "🔪":
            role = discord.utils.get(guild.roles, id=883990208528404510)
            await member.remove_roles(role)
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "🦞":
            role = discord.utils.get(guild.roles, id=849024322181529652)
            await member.remove_roles(role)
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "🚗":
            role = discord.utils.get(guild.roles, id=878159071348396052)
            await member.remove_roles(role)
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "🔧":
            role = discord.utils.get(guild.roles, id=878166632520880169)
            await member.remove_roles(role)
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "🪔":
            role = discord.utils.get(guild.roles, id=853691593277964308)
            await member.remove_roles(role)
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "🚔":
            role = discord.utils.get(guild.roles, id=848834740071956490)
            await member.remove_roles(role)
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "🦐":
            role = discord.utils.get(guild.roles, id=849024325252022282)
            await member.remove_roles(role)
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "🌵":
            role = discord.utils.get(guild.roles, id=849024321401520128)
            await member.remove_roles(role)
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "⭕":
            role = discord.utils.get(guild.roles, id=847805865825796116)
            await member.remove_roles(role)
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "🦀":
            role = discord.utils.get(guild.roles, id=849024324374757397)
            await member.remove_roles(role)
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "💦":
            role = discord.utils.get(guild.roles, id=853691591049740328)
            await member.remove_roles(role)
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "🔊":
            role = discord.utils.get(guild.roles, id=848834726051577916)
            await member.remove_roles(role)
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "💈":
            role = discord.utils.get(guild.roles, id=853691592443691059)
            await member.remove_roles(role)
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "🌊":
            role = discord.utils.get(guild.roles, id=849024324157308928)
            await member.remove_roles(role)
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "🌲":
            role = discord.utils.get(guild.roles, id=849026952585150505)
            await member.remove_roles(role)
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "⚡":
            role = discord.utils.get(guild.roles, id=847805865256157215)
            await member.remove_roles(role)
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "☁️":
            role = discord.utils.get(guild.roles, id=849026952996454470)
            await member.remove_roles(role)
        if payload.message_id == 943518617495023638 and str(payload.emoji) == "🧭":
            role = discord.utils.get(guild.roles, id=853691590214942730)
            await member.remove_roles(role)
        if payload.message_id == 943518619214676028 and str(payload.emoji) == "🌈":
            role = discord.utils.get(guild.roles, id=883990162932113448)
            await member.remove_roles(role)
        if payload.message_id == 943518619214676028 and str(payload.emoji) == "🪓":
            role = discord.utils.get(guild.roles, id=883990161296351282)
            await member.remove_roles(role)
        if payload.message_id == 943518619214676028 and str(payload.emoji) == "🧨":
            role = discord.utils.get(guild.roles, id=883990163448021002)
            await member.remove_roles(role)
        if payload.message_id == 943521694914576464 and str(payload.emoji) == "🎄":
            role = discord.utils.get(guild.roles, id=849026949825036328)
            await member.remove_roles(role)
async def setup(bot):
    await bot.add_cog(reaction_roles(bot))
