import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
intents = discord.Intents.all()
intents.members = True
bot = discord.Client(intents=intents)
from discord.ext import tasks, commands
global voc
global vc
global m
global members
class banner_changing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @tasks.loop(minutes = 6.0)
    async def change_banners(self):
        global m
        global voc
        global vc
        im = Image.new('RGB', (1920,1080), color=('#ffffff'))
        font = ImageFont.truetype("/Users/Artyom/source/repos/main/Aneko bot/shrift/slant.ttf", size=145)
        #/root/python/slant.ttf
        #/Users/Artyom/source/repos/main/Aneko bot/shrift/slant.ttf
        draw_text = ImageDraw.Draw(im)
        draw_text.text(
        (555,806),
        m,
        font=font,
        fill=('#010101')
        )
        draw_text.text(
        (550,800),
        m,
        font=font,
        fill=('#5b5982')
        )
        draw_text.text(
        (1265,806),
        vc,
        font=font,
        fill=('#010101')
        )
        draw_text.text(
        (1260,800),
        vc,
        font=font,
        fill=('#5b5982')
        )
        im.save("text.png", save_all=True)
        im = Image.open("text.png")
        im = im.convert("RGBA")
        datas = im.getdata()
        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        im.putdata(newData)
        im.save("text_2.png", "PNG")
        im1 = Image.open("text_2.png")
        ban = Image.open("banner.png")
        ban.paste(im1, (0,0), im1)
        ban.save("banner_2.png", "PNG")
        file = ("banner_2.png")
        with open(file, 'rb') as f:
            image = f.read()
            guild = self.bot.get_guild(842110386215321650)
        await guild.edit(banner=image)
    @commands.Cog.listener()
    async def on_ready(self):
        global voc
        global vc
        global m
        global members
        voice = set()
        guild = self.bot.get_guild(842110386215321650)
        for v in guild.voice_channels:
            for member in v.members:
                voice.add(member.id)
        voc = len(voice)
        vc = str(voc)
        members =guild.member_count
        m = str(members)
        print(f"Banner Edit is ready!")
        self.change_banners.start()
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after): 
        global voc
        global vc
        if before.channel is None: 
            voc = voc+1
        if after.channel is None:
            voc = voc-1
        vc = str(voc)
        if voc <= 0:
            voc = 0

async def setup(bot):
    await bot.add_cog(banner_changing(bot))
