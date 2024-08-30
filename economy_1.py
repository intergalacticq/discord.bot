from code import interact
from unittest import result
import discord
from discord.ext import tasks,commands
import datetime 
import sqlite3 as sl
from loguru import logger
import random
import asyncio
import enum
import datetime
import threading
from datetime import datetime, timedelta
from discord import app_commands
rnd = random.SystemRandom()
intents = discord.Intents.all()
intents.members = True
bot = discord.Client(intents=intents)
db_lock = threading.Lock()
def execute_query(query, params=None):
    db_lock.acquire()
    try:
        con = sl.connect('aneko.db')
        cursor = con.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        results = cursor.fetchall()
        con.commit()
        con.close()
        return results
    finally:
        db_lock.release()
lb = ['🥇','🥈','🥉','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟']
fish_list = {
    1:{ "name": "Фугу🐡", "price": 250},
    2:{ "name": "Окунь🐟", "price": 50},
    3:{ "name": "Лосось🐟", "price": 150},
    4:{ "name": "Карп🐟", "price": 50},
    5:{ "name": "Тунец🐟", "price": 100},
    6:{ "name": "Кит🐳", "price": 200},
    7:{ "name": "Белуга-альбинос🐠", "price": 225},
    8:{ "name": "Тигровая акула🦈", "price": 280},
    9:{ "name": "Сом🐟", "price": 100},
    10:{ "name": "Треска🐟", "price": 160},
    11:{ "name": "Сазан🐟", "price": 110},
    12:{ "name": "Баса🐟", "price": 140},
    13:{ "name": "Форель🐟", "price": 170},
    14: {"name": "Морской окунь🐟", "price": 200},
    15: {"name": "Акула-молот🦈", "price": 300},
    16: {"name": "Сельдь🐟", "price": 80},
    17: {"name": "Морской лещ🐟", "price": 120},
    18: {"name": "Амур🐟", "price": 130},
    19: {"name": "Мускус🐟", "price": 180},
    20: {"name": "Карась🐟", "price": 90},
    21: {"name": "Бурбот🐟", "price": 110},
    22: {"name": "Щука🐟", "price": 190},
    23: {"name": "Плотва🐟", "price": 70},
    24: {"name": "Кольцевой коралл🌊", "price": 20},
    25: {"name": "Старый сапог🥾", "price": 5},
    26: {"name": "Ржавый ключ🔑", "price": 10},
    27: {"name": "Пластиковая бутылка🍾", "price": 3},
    28: {"name": "Сигаретная упаковка🚬", "price": 2},
    29: {"name": "Пустая жестянка🥫", "price": 4},
    30: {"name": "Пластиковая крышка♻️", "price": 1},
    31:{ "name": "Мусор🗑", "price": 0},
    32:{ "name": "Трусы🩲", "price": 0},
    33:{ "name": "Сандали👞", "price": 0},
    34:{ "name": "Бутылка🍾", "price": 0},
    35: {"name": "Обычный ключ🔑", "price": 0},
    36: {"name": "Серебряный ключ🔑", "price": 0},
    37: {"name": "Золотой ключ🔑", "price": 0}
}
shop_items = {
    1:{"name":"Удочка","price": 50},
    2:{"name":"<@&842326871240605766>","price": 3500, "id": 842326871240605766},
    3:{"name":"<@&842326871928340510>","price": 3500, "id": 842326871928340510},
    4:{"name":"<@&842326870711205908>","price": 3500, "id": 842326870711205908},
    5:{"name":"<@&935290703368577074>","price": 5500, "id": 935290703368577074},
    6:{"name":"<@&842301440193462333>","price": 6500, "id": 842301440193462333},
    7:{"name":"<@&842326869939453983>","price": 6500, "id": 842326869939453983},
    8:{"name":"<@&842326869626060821>","price": 6500, "id": 842326869626060821},
    9:{"name":"<@&842327149162790912>","price": 9000, "id": 842327149162790912},
    10:{"name":"<@&870005613449588846>","price": 10000, "id": 870005613449588846},
    11:{"name":"<@&870005614036783115>","price": 10000, "id": 870005614036783115},
    12:{"name":"<@&870005614322016279>","price": 10000, "id": 870005614322016279},
    13:{"name":"<@&870005615236382792>","price": 10000, "id": 870005615236382792},
    14:{"name":"<@&870005618507927612>","price": 10000, "id": 870005618507927612},
    15:{"name":"<@&870005618637946913>","price": 10000, "id": 870005618637946913},
    16:{"name":"<@&842327149561643010>","price": 13000, "id": 842327149561643010},
    17:{"name":"<@&870005622794485810>","price": 13500, "id": 870005622794485810},
    18:{"name":"<@&934068714549157888>","price": 17000, "id": 934068714549157888},
    19:{"name":"<@&934068715216068678>","price": 18000, "id": 934068715216068678},
    20:{"name":"<@&934068715442548746>","price": 19000, "id": 934068715442548746},
    21:{"name":"<@&842327203026042911>","price": 20000, "id": 842327203026042911},
    22:{"name":"<@&842326869093253120>","price": 21500, "id": 842326869093253120},
    23:{"name":"<@&934068716197539870>","price": 24000, "id": 934068716197539870},
    24:{"name":"<@&870005613151780894>","price": 26000, "id": 870005613151780894},
    25:{"name":"<@&870005616763109456>","price": 29740, "id": 870005616763109456},
    26:{"name":"<@&934068717204144128>","price": 30000, "id": 934068717204144128},
    27:{"name":"<@&934502196832264203>","price": 35000, "id": 934502196832264203},
    28:{"name":"<@&934897790885179422>","price": 40000, "id": 934897790885179422},
    29:{"name":"<@&935061020647493692>","price": 43000, "id": 935061020647493692},
    30:{"name":"<@&935061144345923596>","price": 50000, "id": 935061144345923596},
    31:{"name":"<@&935126058150273096>","price": 55500, "id": 935126058150273096},
    32:{"name":"<@&935244430506594344>","price": 69069, "id": 935244430506594344},
    33:{"name":"<@&935290701682462812>","price": 80000, "id": 935290701682462812},
    34:{"name":"<@&935290702932377610>","price": 90000, "id": 935290702932377610},
    35:{"name":"<@&935290700633878558>","price": 100000, "id": 935290700633878558},
    36:{"name":"<@&934068713739653140>","price": 128000, "id": 934068713739653140},
    37:{"name":"<@&870005623385915454>","price": 2500000, "id": 870005623385915454}
}

class cases(str, enum.Enum):
    Стандартный = "Стандартный"
    Редкий = "Редкий"
    Легендарный = "Легендарный"
class jobs(str, enum.Enum):
    Уборщик = "Уборщик"
    Официант = "Официант"
    Администратор_кафе = "Администратор_кафе"
    Менеджер_по_продажам = "Менеджер_по_продажам"
    Специалист_по_закупкам = "Специалист_по_закупкам"
    Менеджер_по_маркетингу = "Менеджер_по_маркетингу"
    Начальник_отдела = "Начальник_отдела"
    Заместитель_директора = "Заместитель_директора"
    Директор_филиала = "Директор_филиала"
    Генеральный_директор_компании = "Генеральный_директор_компании"

def calculate_points(hand):
            total_points = 0
            num_aces = 0
            skip_next_card = False
            for card in hand:
                if skip_next_card:
                    skip_next_card = False
                    continue
                if card == '1':
                    total_points += 10
                elif card == '0':
                    skip_next_card = True
                elif card.isdigit():
                    total_points += int(card)
                elif card in ['J', 'Q', 'K']:
                    total_points += 10
                elif card == 'A' :
                    num_aces += 1
                    total_points += 11
            while total_points > 21 and num_aces:
                total_points -= 10
                num_aces -= 1
            return total_points
class MyView(discord.ui.View):
    @discord.ui.button(label="В банк",style=discord.ButtonStyle.primary,emoji="🏛") 
    async def a_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(BalanceModaladd())
    @discord.ui.button(label="Снять на руки",style=discord.ButtonStyle.primary,emoji="👐") 
    async def b_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(BalanceModalrem())
class splitforblackjacksecond(discord.ui.View):
    @discord.ui.button(label="Взять карту",style=discord.ButtonStyle.primary) 
    async def blackjack_cardsyes3_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        results = execute_query("SELECT * FROM players WHERE userid=? LIMIT 1",(interaction.user.id,))
        player_hand_2 = results[0][2]
        dealer_hand = results[0][3]
        dealer_cards = ', '.join([dealer_hand[0], 'X'])
        dealer_cards = ', '.join([dealer_hand[0], 'X'])
        player_points_2 = calculate_points(player_hand_2)
        if player_points_2 >21:
            if dealer_hand[0] == '10'or dealer_hand[1] == '10':
                dealer_points = calculate_points(['10'])
            else:
                dealer_points = calculate_points(dealer_hand[0])
            embedVar = discord.Embed(title=f"Перебор в руке! 💥",description=f"\nВаши карты:\n**{player_hand_2}** (Сумма очков - **{player_points_2}**)\nКарты дилера:\n**{dealer_cards}** (Сумма очков - **{dealer_points}**)\n*Нажмите пас*", color=0xe74c3c)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar)
        else:
            deck_str = results[0][4]
            deck = deck_str.split(', ')
            random_card = random.choice(deck)
            execute_query("DELETE FROM players WHERE deck = ? AND userid = ?", (str(random_card), interaction.user.id,))
            player_hand_2 +=', '+random_card
            execute_query("UPDATE players SET player_hand_2=? WHERE userid=?",(player_hand_2,interaction.user.id,))
            results = execute_query("SELECT * FROM players WHERE userid=?",(interaction.user.id,))
            player_hand_2 = results[0][2]
            player_points_2 = calculate_points(player_hand_2)
            if dealer_hand[0] == '10'or dealer_hand[1] == '10':
                dealer_points = calculate_points(['10'])
            else:
                dealer_points = calculate_points(dealer_hand[0])
            if player_points_2 > 21:
                embedVar = discord.Embed(title=f"Перебор в руке! 💥",description=f"\nВаши карты:\n**{player_hand_2}** (Сумма очков - **{player_points_2}**)\nКарты дилера:\n**{dealer_cards}** (Сумма очков - **{dealer_points}**)\n*Нажмите пас*", color=0xe74c3c)
                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                await interaction.response.edit_message(embed=embedVar)
            else:
                dealer_cards = ', '.join([dealer_hand[0], 'X'])
                embedVar = discord.Embed(title="",description=f"## Блэкджек 🃏\n *Вторая рука*", color=0x2f3136)
                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                embedVar.add_field(name="", value=f"Ваши карты (Рука 2)\n**{player_hand_2}** (Сумма очков - **{player_points_2}**)\nКарты дилера:\n**{dealer_cards}**(Сумма очков - **{dealer_points}**+)\n", inline=False)
                await interaction.response.edit_message(embed=embedVar)
    @discord.ui.button(label="Пас",style=discord.ButtonStyle.primary) 
    async def blackjack_cardsno3_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        results = execute_query("SELECT * FROM players WHERE userid=? LIMIT 1",(interaction.user.id,))
        player_hand_2 = results[0][2]
        player_hand = results[0][1]
        dealer_hand = results[0][3]
        deck_str = results[0][4]
        player_points_1 = calculate_points(player_hand)
        player_points_2 = calculate_points(player_hand_2)
        dealer_points = calculate_points(dealer_hand)
        if dealer_points < 21:
            deck = deck_str.split(', ')
            while (dealer_points < 17 and ( dealer_points < player_points_1 or dealer_points < player_points_2)) or ((dealer_points < player_points_1 and dealer_points < player_points_2) and dealer_points < 20):
                random_card = random.choice(deck)
                execute_query("DELETE FROM players WHERE deck = ? AND userid = ?", (str(random_card), interaction.user.id,))
                dealer_hand +=', '+random_card
                dealer_points = calculate_points(dealer_hand)
            execute_query("UPDATE players SET dealer_hand=? WHERE userid=?",(dealer_hand,interaction.user.id,))
        results = execute_query("SELECT * FROM players WHERE userid=? LIMIT 1",(interaction.user.id,))
        dealer_hand = results[0][3]
        dealer_points = calculate_points(dealer_hand)
        if player_points_1 > 21:
            result = "lose"
        if player_points_2 > 21:
            result = "lose"
        if (player_points_1 and player_points_2 < dealer_points) and dealer_points<21:
            result = "lose"
        if dealer_points > 21 and (player_points_1 <= 21 or player_points_2 <= 21):
            result = "win"
        if player_points_1 <= 21 and dealer_points > 21:
            result = "win"
        if player_points_2 <= 21 and dealer_points > 21:
            result = "win"
        if (player_points_1 > dealer_points or player_points_2 > dealer_points) and (player_points_1 <= 21 or player_points_2 <= 21):
            result = "win"
        if (player_points_1 > dealer_points and player_points_2 > dealer_points) or (player_points_1 == dealer_points and player_points_2 == dealer_points):
            result = "winx2"
        if dealer_points > 21 and player_points_1 <= 21 and player_points_2 <= 21:
            result = "winx2"
        if player_points_1 == dealer_points and player_points_2 == dealer_points:
            result = "nnn"
        if player_points_1 > dealer_points and player_points_2 == dealer_points:
            result = "nnn_1"
        if player_points_1 < dealer_points and player_points_2 == dealer_points:
            result = "nnn_2"
        results_2 = execute_query("SELECT inarm FROM economy WHERE userid=? LIMIT 1",(interaction.user.id,))
        finish_inarm =  results_2[0][0]
        if result == "win":
            finish_inarm += bets+bets
            execute_query("UPDATE economy SET inarm=? WHERE userid=?",(finish_inarm,interaction.user.id,))
            embedVar = discord.Embed(title=f"Вы выиграли! 🎉", description=f"\nВаши карты(Рука 1):\n**{player_hand}** (Сумма очков - **{player_points_1}**)\nВаши карты(Рука 2):\n**{player_hand_2}** (Сумма очков - **{player_points_2}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)\n** Ваш выигрыш - {bets+bets}**<:Ametist:1042372594067832882>\n", color=0x2ecc71)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
            await interaction.response.edit_message(embed=embedVar,view=None)
        elif result == "winx2":
            finish_inarm += (bets+bets)*2
            execute_query("UPDATE economy SET inarm=? WHERE userid=?",(finish_inarm,interaction.user.id,))
            embedVar = discord.Embed(title=f"Вы выиграли! 🎉", description=f"\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points_1}**)\nВаши карты(Рука 1):\n**{player_hand_2}** (Сумма очков - **{player_points_2}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков -**{dealer_points}**)\nОго, вам крупно повезло! Обе ваши руки оказались выигрышными, и ваш выигрыш увеличен вдвое!\n**Ваш выигрыш - {(bets+bets)*2}**<:Ametist:1042372594067832882>", color=0x2ecc71)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
            await interaction.response.edit_message(embed=embedVar,view=None)
        elif result == "lose":
            embedVar = discord.Embed(title=f"Вы проиграли. 💔", description=f"\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points_1}**)\nВаши карты(Рука 1):\n**{player_hand_2}** (Сумма очков - **{player_points_2}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)\nВарианты проигрыша:\n1. У дилера столько же или больше очков, чем у вас.\n2. Одна ваша рука - проигрышная, а количество очков во второй руке равно количеству очков у дилера.", color=0xe74c3c)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
            await interaction.response.edit_message(embed=embedVar,view=None)
        elif result == "nnn":
            finish_inarm += bets+bets
            execute_query("UPDATE economy SET inarm=? WHERE userid=?",(finish_inarm,interaction.user.id,))
            embedVar = discord.Embed(title=f"Ничья 🤝", description=f"\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points_1}**)\nВаши карты(Рука 1):\n**{player_hand_2}** (Сумма очков - **{player_points_2}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)\n Деньги не были сняты с баланса.", color=0x979c9f)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
            await interaction.response.edit_message(embed=embedVar,view=None)
        elif result == "nnn_1":
            finish_inarm += bets+bets+bets
            execute_query("UPDATE economy SET inarm=? WHERE userid=?",(finish_inarm,interaction.user.id,))
            embedVar = discord.Embed(title=f"Ничья 🤝", description=f"\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points_1}**)\nВаши карты(Рука 1):\n**{player_hand_2}** (Сумма очков - **{player_points_2}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)\n В этом случае вы получаете - {bets}", color=0x979c9f)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
            await interaction.response.edit_message(embed=embedVar,view=None)
        elif result == "nnn_2":
            finish_inarm += bets
            execute_query("UPDATE economy SET inarm=? WHERE userid=?",(finish_inarm,interaction.user.id,))
            embedVar = discord.Embed(title=f"Ничья 🤝", description=f"\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points_1}**)\nВаши карты(Рука 1):\n**{player_hand_2}** (Сумма очков - **{player_points_2}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)\n В этом случае вы получаете - {bets}", color=0x979c9f)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
            await interaction.response.edit_message(embed=embedVar,view=None)
class splitforblackjackfirst(discord.ui.View):
    @discord.ui.button(label="Взять карту",style=discord.ButtonStyle.primary) 
    async def blackjack_cardsyes2_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        results = execute_query("SELECT * FROM players WHERE userid=? LIMIT 1",(interaction.user.id,))
        player_hand = results[0][1]
        dealer_hand = results[0][3]
        deck_str = results[0][4]
        dealer_cards = ', '.join([dealer_hand[0], 'X'])
        player_points_1 = calculate_points(player_hand)
        if player_points_1 >21:
            if dealer_hand[0] == '10'or dealer_hand[1] == '10':
                dealer_points = calculate_points(['10'])
            else:
                dealer_points = calculate_points(dealer_hand[0])
            embedVar = discord.Embed(title="Перебор в руке! 💥",description=f"\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points_1}**)\nКарты дилера:\n**{dealer_cards}** (Сумма очков - **{dealer_points}**+)\nНачинайте игру на вторую руку.\n\n*Нажмите пас*", color=0xe74c3c)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar)
        else:
            deck = deck_str.split(', ')
            random_card = random.choice(deck)
            execute_query("DELETE FROM players WHERE deck = ? AND userid = ?", (str(random_card), interaction.user.id,))
            player_hand +=', '+random_card
            execute_query("UPDATE players SET player_hand=? WHERE userid=?",(player_hand,interaction.user.id,))
            results_2 = execute_query("SELECT player_hand FROM players WHERE userid=? LIMIT 1",(interaction.user.id,))
            player_hand = results_2[0][0]
            player_points_1 = calculate_points(player_hand)
            if player_points_1 >21:
                if dealer_hand[0] == '10'or dealer_hand[1] == '10':
                    dealer_points = calculate_points(['10'])
                else:
                    dealer_points = calculate_points(dealer_hand[0])
                embedVar = discord.Embed(title="Перебор в руке! 💥",description=f"\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points_1}**)\nКарты дилера:\n**{dealer_cards}**\n(Сумма очков -**{dealer_points}**+)\nНачинайте игру на вторую руку.\n\n*Нажмите пас*", color=0xe74c3c)
                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                await interaction.response.edit_message(embed=embedVar)
            else:
                player_points_1 = calculate_points(player_hand)
                if dealer_hand[0] == '10'or dealer_hand[1] == '10':
                    dealer_points = calculate_points(['10'])
                else:
                    dealer_points = calculate_points(dealer_hand[0])
                dealer_cards = ', '.join([dealer_hand[0], 'X'])
                embedVar = discord.Embed(title="",description=f"## Блэкджек 🃏\n *Первая рука*", color=0x2f3136)
                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                embedVar.add_field(name="", value=f"Ваши карты (Рука 1)\n**{player_hand}** (Сумма очков - **{player_points_1}**)\nКарты дилера:\n**{dealer_cards}**\n(Сумма очков - **{dealer_points}**)\n", inline=False)
                await interaction.response.edit_message(embed=embedVar)
    @discord.ui.button(label="Пас",style=discord.ButtonStyle.primary) 
    async def blackjack_cardsno2_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        results = execute_query("SELECT * FROM players WHERE userid=? LIMIT 1",(interaction.user.id,))
        player_hand_2 = results[0][2]
        dealer_hand = results[0][3]
        dealer_cards = ', '.join([dealer_hand[0], 'X'])
        player_points_2 = calculate_points(player_hand_2)
        if dealer_hand[0] == '10'or dealer_hand[1] == '10':
            dealer_points = calculate_points(['10'])
        else:
            dealer_points = calculate_points(dealer_hand[0])
        embedVar = discord.Embed(title="",description=f"## Блэкджек 🃏\n *Вторая рука*", color=0x2f3136)
        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
        embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
        embedVar.add_field(name="", value=f"Ваши карты (Рука 2)\n**{player_hand_2}** (Сумма очков - **{player_points_2}**)\nКарты дилера:\n**{dealer_cards}** (Сумма очков - **{dealer_points}**)\n", inline=False)
        view = splitforblackjacksecond(timeout=None)
        await interaction.response.edit_message(embed=embedVar, view=view)

class triviacheckView(discord.ui.View):

    @discord.ui.button(label="",style=discord.ButtonStyle.primary,emoji="1️⃣") 
    async def one_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        global answer_id
        global user_on_inter
        answer_id
        results = execute_query("SELECT correct_answer FROM trivia WHERE id = ? LIMIT 1",(answer_id,))
        question = results[0][0]
        selected_answer_index = 1
        if selected_answer_index == question:
            results = execute_query("SELECT inarm FROM economy WHERE userid=? LIMIT 1",(interaction.user.id,))
            inarms = results[0][0]
            inarms +=450
            execute_query("UPDATE economy SET inarm = ? WHERE userid = ?",(inarms,interaction.user.id,))
            embedVar = discord.Embed(title="Правильный ответ!", description=f"Вы получаете награду - 450<:Ametist:1042372594067832882>", color=0x2ecc71)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar,view=None)
        else:
            embedVar = discord.Embed(title="Неправильный ответ.", description=f"Вы не получаете награду.", color=0xe74c3c)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar,view=None)
    @discord.ui.button(label="",style=discord.ButtonStyle.primary,emoji="2️⃣") 
    async def two_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        global answer_id
        global user_on_inter
        answer_id
        results = execute_query("SELECT correct_answer FROM trivia WHERE id = ? LIMIT 1",(answer_id,))
        question = results[0][0]
        selected_answer_index = 2
        if selected_answer_index == question:
            results = execute_query("SELECT inarm FROM economy WHERE userid=? LIMIT 1",(interaction.user.id,))
            inarms = results[0][0]
            inarms +=450
            execute_query("UPDATE economy SET inarm = ? WHERE userid = ?",(inarms,interaction.user.id,))
            embedVar = discord.Embed(title="Правильный ответ!", description=f"Вы получаете награду - 450<:Ametist:1042372594067832882>", color=0x2ecc71)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar,view=None)
        else:
            embedVar = discord.Embed(title="Неправильный ответ.", description=f"Вы не получаете награду.", color=0xe74c3c)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar,view=None)
    @discord.ui.button(label="",style=discord.ButtonStyle.primary,emoji="3️⃣") 
    async def three_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        global answer_id
        global user_on_inter
        answer_id
        results = execute_query("SELECT correct_answer FROM trivia WHERE id = ? LIMIT 1",(answer_id,))
        question = results[0][0]
        selected_answer_index = 3
        if selected_answer_index == question:
            results = execute_query("SELECT inarm FROM economy WHERE userid=? LIMIT 1",(interaction.user.id,))
            inarms = results[0][0]
            inarms +=450
            execute_query("UPDATE economy SET inarm = ? WHERE userid = ?",(inarms,interaction.user.id,))
            embedVar = discord.Embed(title="Правильный ответ!", description=f"Вы получаете награду - 450<:Ametist:1042372594067832882>", color=0x2ecc71)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar,view=None)
        else:
            embedVar = discord.Embed(title="Неправильный ответ.", description=f"Вы не получаете награду.", color=0xe74c3c)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar,view=None)
    @discord.ui.button(label="",style=discord.ButtonStyle.primary,emoji="4️⃣") 
    async def four_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        global answer_id
        global user_on_inter
        answer_id
        results = execute_query("SELECT correct_answer FROM trivia WHERE id = ? LIMIT 1",(answer_id,))
        question = results[0][0]
        selected_answer_index = 4
        if selected_answer_index == question:
            results = execute_query("SELECT inarm FROM economy WHERE userid=? LIMIT 1",(interaction.user.id,))
            inarms = results[0][0]
            inarms +=450
            execute_query("UPDATE economy SET inarm = ? WHERE userid = ?",(inarms,interaction.user.id,))
            embedVar = discord.Embed(title="Правильный ответ!", description=f"Вы получаете награду - 450<:Ametist:1042372594067832882>", color=0x2ecc71)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar,view=None)
        else:
            embedVar = discord.Embed(title="Неправильный ответ.", description=f"Вы не получаете награду.", color=0xe74c3c)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar,view=None)
class triviaView(discord.ui.View):

    @discord.ui.button(label="",style=discord.ButtonStyle.primary,emoji="1️⃣") 
    async def one_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        #география
        global trivia_category_id
        global answer_id
        trivia_category_id = 1
        results = execute_query("SELECT * FROM trivia WHERE category_id = 1 ORDER BY RANDOM() LIMIT 1")
        question = results[0][1]
        answer_id = results[0][6]
        embedVar = discord.Embed(title="География 🌍", description="", color=discord.Color.blue())
        embedVar.add_field(name=f"{question}", value="", inline=False)
        answers = [results[0][i] for i in range(2, 6)]  
        for i, answer in enumerate(answers, start=1):
            embedVar.add_field(name=f"", value=f"{i}. {answer}", inline=False)
        view = triviacheckView(timeout=45)
        await interaction.response.edit_message(embed=embedVar,view=view)
    @discord.ui.button(label="",style=discord.ButtonStyle.primary,emoji="2️⃣") 
    async def two_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        #математика
        global answer_id
        global trivia_category_id_2
        trivia_category_id_2 = 2
        results = execute_query("SELECT * FROM trivia WHERE category_id = 2 ORDER BY RANDOM() LIMIT 1")
        question = results[0][1]
        answer_id = results[0][6]
        embedVar = discord.Embed(title="Математика 🔢", description="", color=discord.Color.blue())
        embedVar.add_field(name=f"{question}", value="", inline=False)
        answers = [results[0][i] for i in range(2, 6)] 
        for i, answer in enumerate(answers, start=1):
            embedVar.add_field(name=f"", value=f"{i}. {answer}", inline=False)
        view = triviacheckView(timeout=45)
        await interaction.response.edit_message(embed=embedVar,view=view)
    @discord.ui.button(label="",style=discord.ButtonStyle.primary,emoji="3️⃣") 
    async def three_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        #физика
        global answer_id
        global trivia_category_id_3
        trivia_category_id_3 = 3
        results = execute_query("SELECT * FROM trivia WHERE category_id = 3 ORDER BY RANDOM() LIMIT 1")
        question = results[0][1]
        answer_id = results[0][6]
        embedVar = discord.Embed(title="Физика 🌡", description="", color=discord.Color.blue())
        embedVar.add_field(name=f"{question}", value="", inline=False)
        answers = [results[0][i] for i in range(2, 6)]
        for i, answer in enumerate(answers, start=1):
            embedVar.add_field(name=f"", value=f"{i}. {answer}", inline=False)
        view = triviacheckView(timeout=45)
        await interaction.response.edit_message(embed=embedVar,view=view)
    @discord.ui.button(label="",style=discord.ButtonStyle.primary,emoji="4️⃣") 
    async def four_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        #химия
        global answer_id
        global trivia_category_id_4
        trivia_category_id_4 = 4
        results = execute_query("SELECT * FROM trivia WHERE category_id = 4 ORDER BY RANDOM() LIMIT 1")
        question = results[0][1]
        answer_id = results[0][6]
        embedVar = discord.Embed(title="Химимя 💧", description="", color=discord.Color.blue())
        embedVar.add_field(name=f"{question}", value="", inline=False)
        answers = [results[0][i] for i in range(2, 6)]
        for i, answer in enumerate(answers, start=1):
            embedVar.add_field(name=f"", value=f"{i}. {answer}", inline=False)
        view = triviacheckView(timeout=45)
        await interaction.response.edit_message(embed=embedVar,view=view)
    @discord.ui.button(label="",style=discord.ButtonStyle.primary,emoji="5️⃣") 
    async def five_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        #интернет
        global answer_id
        global trivia_category_id_5
        trivia_category_id_5 = 5
        results = execute_query("SELECT * FROM trivia WHERE category_id = 5 ORDER BY RANDOM() LIMIT 1")
        question = results[0][1]
        answer_id = results[0][6]
        embedVar = discord.Embed(title="Интернет 🌐", description="", color=discord.Color.blue())
        embedVar.add_field(name=f"{question}", value="", inline=False)
        answers = [results[0][i] for i in range(2, 6)]
        for i, answer in enumerate(answers, start=1):
            embedVar.add_field(name=f"", value=f"{i}. {answer}", inline=False)
        view = triviacheckView(timeout=45)
        await interaction.response.edit_message(embed=embedVar,view=view)
    @discord.ui.button(label="",style=discord.ButtonStyle.primary,emoji="6️⃣") 
    async def six_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        #аниме
        global answer_id
        global trivia_category_id_6
        trivia_category_id_6 = 6
        results = execute_query("SELECT * FROM trivia WHERE category_id = 6 ORDER BY RANDOM() LIMIT 1")
        question = results[0][1]
        answer_id = results[0][6]
        embedVar = discord.Embed(title="Аниме 🍜", description="", color=discord.Color.blue())
        embedVar.add_field(name=f"{question}", value="", inline=False)
        answers = [results[0][i] for i in range(2, 6)]
        for i, answer in enumerate(answers, start=1):
            embedVar.add_field(name=f"", value=f"{i}. {answer}", inline=False)
        view = triviacheckView(timeout=45)
        await interaction.response.edit_message(embed=embedVar,view=view)
    @discord.ui.button(label="",style=discord.ButtonStyle.primary,emoji="7️⃣") 
    async def seven_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        #спорт
        global answer_id
        global trivia_category_id_7
        trivia_category_id_7 = 7
        results = execute_query("SELECT * FROM trivia WHERE category_id = 7 ORDER BY RANDOM() LIMIT 1")
        question = results[0][1]
        answer_id = results[0][6]
        embedVar = discord.Embed(title="Спорт ⚽", description="", color=discord.Color.blue())
        embedVar.add_field(name=f"{question}", value="", inline=False)
        answers = [results[0][i] for i in range(2, 6)]
        for i, answer in enumerate(answers, start=1):
            embedVar.add_field(name=f"", value=f"{i}. {answer}", inline=False)
        view = triviacheckView(timeout=45)
        await interaction.response.edit_message(embed=embedVar,view=view)
    @discord.ui.button(label="",style=discord.ButtonStyle.primary,emoji="8️⃣") 
    async def eight_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        #фильмы
        global answer_id
        global trivia_category_id_7
        trivia_category_id_7 = 8
        results = execute_query("SELECT * FROM trivia WHERE category_id = 8 ORDER BY RANDOM() LIMIT 1")
        question = results[0][1]
        answer_id = results[0][6]
        embedVar = discord.Embed(title="Фильмы 🎞", description="", color=discord.Color.blue())
        embedVar.add_field(name=f"{question}", value="", inline=False)
        answers = [results[0][i] for i in range(2, 6)]
        for i, answer in enumerate(answers, start=1):
            embedVar.add_field(name=f"", value=f"{i}. {answer}", inline=False)
        view = triviacheckView(timeout=45)
        await interaction.response.edit_message(embed=embedVar,view=view)
    @discord.ui.button(label="",style=discord.ButtonStyle.primary,emoji="9️⃣") 
    async def nine_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        #музыка
        global answer_id
        global trivia_category_id_7
        trivia_category_id_7 = 9
        results = execute_query("SELECT * FROM trivia WHERE category_id = 9 ORDER BY RANDOM() LIMIT 1")
        question = results[0][1]
        answer_id = results[0][6]
        embedVar = discord.Embed(title="Музыка 🎵", description="", color=discord.Color.blue())
        embedVar.add_field(name=f"{question}", value="", inline=False)
        answers = [results[0][i] for i in range(2, 6)]
        for i, answer in enumerate(answers, start=1):
            embedVar.add_field(name=f"", value=f"{i}. {answer}", inline=False)
        view = triviacheckView(timeout=45)
        await interaction.response.edit_message(embed=embedVar,view=view)
    @discord.ui.button(label="",style=discord.ButtonStyle.primary,emoji="🔟") 
    async def ten_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        #авто
        global answer_id
        global trivia_category_id_7
        trivia_category_id_7 = 10
        results = execute_query("SELECT * FROM trivia WHERE category_id = 10 ORDER BY RANDOM() LIMIT 1")
        question = results[0][1]
        answer_id = results[0][6]
        embedVar = discord.Embed(title="Автомобили 🚘", description="", color=discord.Color.blue())
        embedVar.add_field(name=f"{question}", value="", inline=False)
        answers = [results[0][i] for i in range(2, 6)]
        for i, answer in enumerate(answers, start=1):
            embedVar.add_field(name=f"", value=f"{i}. {answer}", inline=False)
        view = triviacheckView(timeout=45)
        await interaction.response.edit_message(embed=embedVar,view=view)
class BlackjackView(discord.ui.View):

    @discord.ui.button(label="Взять карту",style=discord.ButtonStyle.primary) 
    async def blackjack_cardsyes_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        results = execute_query("SELECT * FROM players WHERE userid=? LIMIT 1",(interaction.user.id,))
        player_hand = results[0][1]
        deck_str = results[0][4]
        dealer_hand = results[0][3]
        dealer_cards = ', '.join([dealer_hand[0], 'X'])
        deck = deck_str.split(', ')
        random_card = random.choice(deck)
        execute_query("DELETE FROM players WHERE deck = ? AND userid = ?", (str(random_card), interaction.user.id,))
        player_hand +=', '+random_card
        execute_query("UPDATE players SET player_hand=? WHERE userid=?",(player_hand,interaction.user.id,))
        player_points = calculate_points(player_hand)
        if player_points > 21:
            if dealer_hand[0] == '10'or dealer_hand[1] == '10':
                dealer_points = calculate_points(['10'])
            else:
                dealer_points = calculate_points(dealer_hand)
            embedVar = discord.Embed(title=f"Вы проиграли! 💔", description=f"Перебор карт.\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)", color=0xe74c3c)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar,view = None)
            execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
            return
        elif player_points == 21:
            results_2 = execute_query("SELECT inarm FROM economy WHERE userid=? LIMIT 1",(interaction.user.id,))
            finish_inarm =  results_2[0][0]
            
            while calculate_points(dealer_hand) < calculate_points(player_hand) and calculate_points(dealer_hand)<21:
                results_3 = execute_query("SELECT deck FROM players WHERE userid = ? LIMIT 1",(interaction.user.id,))
                deck_str = results_3[0][0]
                deck = deck_str.split(', ')
                random_card = random.choice(deck)
                execute_query("DELETE FROM players WHERE deck = ? AND userid = ?", (str(random_card), interaction.user.id,))
                dealer_hand +=', '+random_card
            execute_query("UPDATE players SET dealer_hand=? WHERE userid=?",(dealer_hand,interaction.user.id,))
            if dealer_hand[0] == '10'or dealer_hand[1] == '10':
                dealer_points = calculate_points(['10'])
            else:
                dealer_points = calculate_points(dealer_hand)
            if player_points > 21:
                finish_inarm -=bets
                execute_query("UPDATE economy SET inarm=? WHERE userid=?",(finish_inarm,interaction.user.id,))
                embedVar = discord.Embed(title=f"У вас перебор! 💥", description=f"Вы проиграли.\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)", color=0xe74c3c)
                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                await interaction.response.edit_message(embed=embedVar, view = None)
                execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
                
            elif dealer_points > 21:
                finish_inarm +=bets+bets
                execute_query("UPDATE economy SET inarm=? WHERE userid=?",(finish_inarm,interaction.user.id,))
                embedVar = discord.Embed(title=f"У дилера перебор! 💥🃏", description=f"Вы выиграли.\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)\n**Ваш выигрыш - {bets+bets}**<:Ametist:1042372594067832882>", color=0x2ecc71)
                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                await interaction.response.edit_message(embed=embedVar, view = None)
                execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
            elif player_points > dealer_points:
                finish_inarm +=bets+bets
                execute_query("UPDATE economy SET inarm=? WHERE userid=?",(finish_inarm,interaction.user.id,))
                embedVar = discord.Embed(title=f"Вы выиграли! 🎉", description=f"У вас было больше очков, чем у дилера\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)\n**Ваш выигрыш - {bets+bets}**<:Ametist:1042372594067832882>", color=0x2ecc71)
                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                await interaction.response.edit_message(embed=embedVar, view = None)
                execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
            elif player_points < dealer_points:
                embedVar = discord.Embed(title=f"Вы проиграли. 💔", description=f"У дилера было больше очков, чем у вас\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)", color=0xe74c3c)
                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                await interaction.response.edit_message(embed=embedVar, view = None)
                execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
            else:
                finish_inarm +=bets
                execute_query("UPDATE economy SET inarm = ? WHERE userid = ?", (finish_inarm, interaction.user.id,))
                embedVar = discord.Embed(title=f"Ничья. 🤝", description=f"Деньги не были сняты с баланса\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)", color=0x979c9f)
                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                await interaction.response.edit_message(embed=embedVar, view = None)
                execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
        else:
            if dealer_hand[0] == '10'or dealer_hand[1] == '10':
                dealer_points = calculate_points(['10'])
            else:
                dealer_points = calculate_points(dealer_hand[0])
            results = execute_query("SELECT * FROM players WHERE userid=? LIMIT 1",(interaction.user.id,))
            player_hand = results[0][1]
            dealer_hand = results[0][3]
            dealer_cards = ', '.join([dealer_hand[0], 'X'])
            embedVar = discord.Embed(title=f"", description=f" ## Блэкджэк 🃏\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_cards}** (Сумма очков - **{dealer_points}**+)", color=0x2f3136)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar)
    @discord.ui.button(label="Пас",style=discord.ButtonStyle.primary) 
    async def blackjack_cardsno_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        results = execute_query("SELECT * FROM players WHERE userid=? LIMIT 1",(interaction.user.id,))
        player_hand = results[0][1]
        dealer_hand = results[0][3]
        while calculate_points(dealer_hand) < calculate_points(player_hand) and calculate_points(dealer_hand)<21:
            results_deck = execute_query("SELECT deck FROM players WHERE userid = ? LIMIT 1",(interaction.user.id,))
            deck_str = results_deck[0][0]
            deck = deck_str.split(', ')
            random_card = random.choice(deck)
            execute_query("DELETE FROM players WHERE deck = ? AND userid = ?", (str(random_card), interaction.user.id,))
            dealer_hand +=', '+random_card
        execute_query("UPDATE players SET dealer_hand=? WHERE userid=?",(dealer_hand,interaction.user.id,))
        player_points = calculate_points(player_hand)
        if dealer_hand[0] == '10'or dealer_hand[1] == '10':
            dealer_points = calculate_points(['10'])
        else:
            dealer_points = calculate_points(dealer_hand)
        results_mon = execute_query("SELECT inarm FROM economy WHERE userid=? LIMIT 1",(interaction.user.id,))
        finish_inarm =  results_mon[0][0]
        if player_points > 21:
            finish_inarm -=bets
            execute_query("UPDATE economy SET inarm=? WHERE userid=?",(finish_inarm,interaction.user.id,))
            embedVar = discord.Embed(title=f"У вас перебор! 💥", description=f"Вы проиграли.\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)", color=0xe74c3c)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar, view = None)
            execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
        elif dealer_points > 21:
            finish_inarm +=bets+bets
            execute_query("UPDATE economy SET inarm=? WHERE userid=?",(finish_inarm,interaction.user.id,))
            embedVar = discord.Embed(title=f"У дилера перебор! 💥🃏", description=f"Вы выиграли.\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)\n**Ваш выигрыш - {bets+bets}**<:Ametist:1042372594067832882>", color=0x2ecc71)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar, view = None)
            execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
        elif player_points > dealer_points:
            finish_inarm +=bets+bets
            execute_query("UPDATE economy SET inarm=? WHERE userid=?",(finish_inarm,interaction.user.id,))
            embedVar = discord.Embed(title=f"Вы выиграли! 🎉", description=f"У вас было больше очков, чем у дилера\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)\n**Ваш выигрыш - {bets+bets}**<:Ametist:1042372594067832882>", color=0x2ecc71)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar, view = None)
            execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
            
        elif player_points < dealer_points:

            embedVar = discord.Embed(title=f"Вы проиграли. 💔", description=f"У дилера было больше очков, чем у вас\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)", color=0xe74c3c)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar, view = None)
            execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
        else:
            finish_inarm +=bets
            execute_query("UPDATE economy SET inarm = ? WHERE userid = ?", (finish_inarm, interaction.user.id,))
            embedVar = discord.Embed(title=f"Ничья. 🤝", description=f"Деньги не были сняты с баланса\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)", color=0x979c9f)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar, view = None)
            execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))    
class BlackjackView_2(discord.ui.View):

    @discord.ui.button(label="Взять карту",style=discord.ButtonStyle.primary) 
    async def blackjack_cardsyes_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        results = execute_query("SELECT * FROM players WHERE userid=? LIMIT 1",(interaction.user.id,))
        player_hand = results[0][1]
        deck_str = results[0][4]
        dealer_hand = results[0][3]
        dealer_cards = ', '.join([dealer_hand[0], 'X'])
        deck = deck_str.split(', ')
        random_card = random.choice(deck)
        execute_query("DELETE FROM players WHERE deck = ? AND userid = ?", (str(random_card), interaction.user.id,))
        player_hand +=', '+random_card
        execute_query("UPDATE players SET player_hand=? WHERE userid=?",(player_hand,interaction.user.id,))
        player_points = calculate_points(player_hand)
        if player_points > 21:
            if dealer_hand[0] == '10'or dealer_hand[1] == '10':
                dealer_points = calculate_points(['10'])
            else:
                dealer_points = calculate_points(dealer_hand)
            embedVar = discord.Embed(title=f"Вы проиграли! 💔", description=f"Перебор карт.\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)", color=0xe74c3c)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar,view = None)
            execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
            return
        elif player_points == 21:
            results_2 = execute_query("SELECT inarm FROM economy WHERE userid=? LIMIT 1",(interaction.user.id,))
            finish_inarm =  results_2[0][0]
            
            while calculate_points(dealer_hand) < calculate_points(player_hand) and calculate_points(dealer_hand)<21:
                results_3 = execute_query("SELECT deck FROM players WHERE userid = ? LIMIT 1",(interaction.user.id,))
                deck_str = results_3[0][0]
                deck = deck_str.split(', ')
                random_card = random.choice(deck)
                execute_query("DELETE FROM players WHERE deck = ? AND userid = ?", (str(random_card), interaction.user.id,))
                dealer_hand +=', '+random_card
            execute_query("UPDATE players SET dealer_hand=? WHERE userid=?",(dealer_hand,interaction.user.id,))
            if dealer_hand[0] == '10'or dealer_hand[1] == '10':
                dealer_points = calculate_points(['10'])
            else:
                dealer_points = calculate_points(dealer_hand)
            if player_points > 21:
                finish_inarm -=bets
                execute_query("UPDATE economy SET inarm=? WHERE userid=?",(finish_inarm,interaction.user.id,))
                embedVar = discord.Embed(title=f"У вас перебор! 💥", description=f"Вы проиграли.\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)", color=0xe74c3c)
                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                await interaction.response.edit_message(embed=embedVar, view = None)
                execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
                
            elif dealer_points > 21:
                finish_inarm +=bets+bets
                execute_query("UPDATE economy SET inarm=? WHERE userid=?",(finish_inarm,interaction.user.id,))
                embedVar = discord.Embed(title=f"У дилера перебор! 💥🃏", description=f"Вы выиграли.\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)\n**Ваш выигрыш - {bets+bets}**<:Ametist:1042372594067832882>", color=0x2ecc71)
                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                await interaction.response.edit_message(embed=embedVar, view = None)
                execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
            elif player_points > dealer_points:
                finish_inarm +=bets+bets
                execute_query("UPDATE economy SET inarm=? WHERE userid=?",(finish_inarm,interaction.user.id,))
                embedVar = discord.Embed(title=f"Вы выиграли! 🎉", description=f"У вас было больше очков, чем у дилера\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)\n**Ваш выигрыш - {bets+bets}**<:Ametist:1042372594067832882>", color=0x2ecc71)
                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                await interaction.response.edit_message(embed=embedVar, view = None)
                execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
            elif player_points < dealer_points:
                embedVar = discord.Embed(title=f"Вы проиграли. 💔", description=f"У дилера было больше очков, чем у вас\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)", color=0xe74c3c)
                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                await interaction.response.edit_message(embed=embedVar, view = None)
                execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
            else:
                finish_inarm +=bets
                execute_query("UPDATE economy SET inarm = ? WHERE userid = ?", (finish_inarm, interaction.user.id,))
                embedVar = discord.Embed(title=f"Ничья. 🤝", description=f"Деньги не были сняты с баланса\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)", color=0x979c9f)
                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                await interaction.response.edit_message(embed=embedVar, view = None)
                execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
        else:
            if dealer_hand[0] == '10'or dealer_hand[1] == '10':
                dealer_points = calculate_points(['10'])
            else:
                dealer_points = calculate_points(dealer_hand[0])
            results = execute_query("SELECT player_hand FROM players WHERE userid=? LIMIT 1",(interaction.user.id,))
            player_hand = results[0][1]
            dealer_hand = results[0][3]
            dealer_cards = ', '.join([dealer_hand[0], 'X'])
            embedVar = discord.Embed(title=f"", description=f" ## Блэкджэк 🃏\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_cards}** (Сумма очков - **{dealer_points}**+)", color=0x2f3136)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar)
    @discord.ui.button(label="Пас",style=discord.ButtonStyle.primary) 
    async def blackjack_cardsno_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        results = execute_query("SELECT * FROM players WHERE userid=? LIMIT 1",(interaction.user.id,))
        player_hand = results[0][1]
        dealer_hand = results[0][3]
        while calculate_points(dealer_hand) < calculate_points(player_hand) and calculate_points(dealer_hand)<21:
            results_deck = execute_query("SELECT deck FROM players WHERE userid = ? LIMIT 1",(interaction.user.id,))
            deck_str = results_deck[0][0]
            deck = deck_str.split(', ')
            random_card = random.choice(deck)
            execute_query("DELETE FROM players WHERE deck = ? AND userid = ?", (str(random_card), interaction.user.id,))
            dealer_hand +=', '+random_card
        execute_query("UPDATE players SET dealer_hand=? WHERE userid=?",(dealer_hand,interaction.user.id,))
        player_points = calculate_points(player_hand)
        if dealer_hand[0] == '10'or dealer_hand[1] == '10':
            dealer_points = calculate_points(['10'])
        else:
            dealer_points = calculate_points(dealer_hand)
        results_mon = execute_query("SELECT inarm FROM economy WHERE userid=? LIMIT 1",(interaction.user.id,))
        finish_inarm =  results_mon[0][0]
        if player_points > 21:
            finish_inarm -=bets
            execute_query("UPDATE economy SET inarm=? WHERE userid=?",(finish_inarm,interaction.user.id,))
            embedVar = discord.Embed(title=f"У вас перебор! 💥", description=f"Вы проиграли.\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)", color=0xe74c3c)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar, view = None)
            execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
        elif dealer_points > 21:
            finish_inarm +=bets+bets
            execute_query("UPDATE economy SET inarm=? WHERE userid=?",(finish_inarm,interaction.user.id,))
            embedVar = discord.Embed(title=f"У дилера перебор! 💥🃏", description=f"Вы выиграли.\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)\n**Ваш выигрыш - {bets+bets}**<:Ametist:1042372594067832882>", color=0x2ecc71)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar, view = None)
            execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
        elif player_points > dealer_points:
            finish_inarm +=bets+bets
            execute_query("UPDATE economy SET inarm=? WHERE userid=?",(finish_inarm,interaction.user.id,))
            embedVar = discord.Embed(title=f"Вы выиграли! 🎉", description=f"У вас было больше очков, чем у дилера\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)\n**Ваш выигрыш - {bets+bets}**<:Ametist:1042372594067832882>", color=0x2ecc71)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar, view = None)
            execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
            
        elif player_points < dealer_points:

            embedVar = discord.Embed(title=f"Вы проиграли. 💔", description=f"У дилера было больше очков, чем у вас\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)", color=0xe74c3c)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar, view = None)
            execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))
        else:
            finish_inarm +=bets
            execute_query("UPDATE economy SET inarm = ? WHERE userid = ?", (finish_inarm, interaction.user.id,))
            embedVar = discord.Embed(title=f"Ничья. 🤝", description=f"Деньги не были сняты с баланса\nВаши карты:\n**{player_hand}** (Сумма очков - **{player_points}**)\nКарты дилера:\n**{dealer_hand}** (Сумма очков - **{dealer_points}**)", color=0x979c9f)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.edit_message(embed=embedVar, view = None)
            execute_query("DELETE FROM players WHERE userid = ?",(interaction.user.id,))    
            
    @discord.ui.button(label="Сплит", style=discord.ButtonStyle.primary)
    async def split_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        results = execute_query("SELECT * FROM players WHERE userid=?",(interaction.user.id,))
        player_hand = results[0][1]
        deck_str = results[0][4]
        results_mon = execute_query("SELECT inarm FROM economy WHERE userid = ? LIMIT 1",(interaction.user.id,))
        money_inarm = results_mon[0][0]
        if bets <= money_inarm:
            newinarms = money_inarm-bets
            execute_query("UPDATE economy SET inarm = ? WHERE userid = ?",(newinarms,interaction.user.id,))
            split_or = player_hand.split(', ')
            if len(split_or) == 2 and len(set(split_or)) == 1:
                deck = deck_str.split(', ')
                random_card = random.choice(deck)
                execute_query("DELETE FROM players WHERE deck = ? AND userid = ?", (str(random_card), interaction.user.id,))
                player_hand +=', '+random_card
                execute_query("UPDATE players SET player_hand=? WHERE userid=?",(player_hand,interaction.user.id,))

                results = execute_query("SELECT * FROM players WHERE userid=?",(interaction.user.id,))
                player_hand = results[0][1]
                player_hand_2 = results[0][2]
                split_or = player_hand.split(', ')
                split_or_del = split_or[0]
                split_or.remove(split_or_del)
                player_hand_new =", ".join(split_or)
                execute_query("UPDATE players SET player_hand = ? WHERE userid = ?", (player_hand_new, interaction.user.id))
                random_card_2 = random.choice(deck)
                if player_hand[0] == '10':
                    player_hand_2 = ['10', str(random_card_2)]
                else:
                    player_hand_2 = [str(split_or[0]), str(random_card_2)]
                player_hand_2 = ', '.join(player_hand_2)
                execute_query("UPDATE players SET player_hand_2 = ? WHERE userid = ?",(str(player_hand_2),interaction.user.id,))
                execute_query("DELETE FROM players WHERE deck = ? AND userid = ?", (str(random_card_2), interaction.user.id,))
                results = execute_query("SELECT * FROM players WHERE userid=? LIMIT 1",(interaction.user.id,))
                dealer_hand = results[0][3]
                dealer_cards = ', '.join([dealer_hand[0], 'X'])
                player_hand = results[0][1]
                player_hand_2 = results[0][2]
                player_points_1 = calculate_points(player_hand)
                player_points_2 = calculate_points(player_hand_2)
                embedVar = discord.Embed(title="",description=f"## Блэкджек 🃏\n **Игра на первую руку(Рука 1).**", color=interaction.user.color)
                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                embedVar.add_field(name="", value=f"**Ваши карты (Рука 1)**\n**{player_hand}** (Сумма очков -**{player_points_1}**)\n**Ваши карты (Рука 2)**\n**{player_hand_2}** (Сумма очков -**{player_points_2}**)\n**Карты дилера**\n**{dealer_cards}**", inline=False)
                view = splitforblackjackfirst(timeout=None)
                await interaction.response.edit_message(embed=embedVar,view=view)
            else:
                embedVar = discord.Embed(title="", description=f"Невозможно сделать сплит с текущими картами.", color=interaction.user.color)
                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                await interaction.response.send_message(embed=embedVar, ephemeral=True)
        else:
            embedVar = discord.Embed(title="У вас на руках недостаточно денег, чтобы начать сплит", description=f"Снимите деньги на руки в размере {bets}, чтобы начать сплит", color=interaction.user.color)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.send_message(embed=embedVar, ephemeral=True)
class BalanceModaladd(discord.ui.Modal, title='Ввод суммы'):
    bot = commands.Bot
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.TextInput(label='Введите сумму, которую перевести в банк', style=discord.TextStyle.short, required=True, max_length=6))
    async def on_submit(self, interaction: discord.Interaction):
        summ_val = self.children[0].value
        try:
            results = execute_query("SELECT bank, inarm,total FROM economy WHERE userid = ? LIMIT 1",(interaction.user.id,))
            bank = results[0][0]
            inarm = results[0][1]
            try:
                summ_val = int(summ_val)
                if summ_val >0:
                    if summ_val <= inarm:
                        newbank = int(bank)+int(summ_val)
                        execute_query("UPDATE economy SET bank = ? WHERE userid = ?", (newbank, interaction.user.id,))
                        newinarm = inarm-summ_val
                        execute_query("UPDATE economy SET inarm = ? WHERE userid = ?", (newinarm, interaction.user.id,))
                        embedVar = discord.Embed(title="Новый баланс 🏛", description="", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                        results = execute_query("SELECT bank, inarm FROM economy WHERE userid = ?", (interaction.user.id,))
                        bank = results[0][0]
                        inarm = results[0][1]
                        total = int(bank)+int(inarm)
                        execute_query("UPDATE economy SET total = ? WHERE userid = ?", (total, interaction.user.id,))
                        embedVar.add_field(name="На руках", value=f'{inarm} <:Ametist:1042372594067832882>', inline=False)
                        embedVar.add_field(name="В банке", value=f'{bank} <:Ametist:1042372594067832882>', inline=False)
                        embedVar.add_field(name="Всего", value=f'{total} <:Ametist:1042372594067832882>', inline=False)
                        embedVar.add_field(name="📗Инструкция.", value=f"Чтобы перевести все деньги сразу, вы можете ввести вместо числа all/всё/все", inline=False)
        
                        await interaction.response.edit_message(embed=embedVar)
                    else:
                        await interaction.response.send_message("Вы указали число, превышающее количество денег на руках",ephemeral=True)
                else:
                    await interaction.response.send_message("Введённая вами сумма должна быть больше нуля.", ephemeral = True)
            except:
                summ_val_lower = summ_val.lower()
                if summ_val_lower == "все" or summ_val_lower == "всё" or summ_val_lower == "all":
                    newbank = int(bank)+int(inarm)
                    execute_query("UPDATE economy SET bank = ? WHERE userid = ?", (newbank, interaction.user.id,))
                    newinarm = 0
                    execute_query("UPDATE economy SET inarm = ? WHERE userid = ?", (newinarm, interaction.user.id,))
                    embedVar = discord.Embed(title="Новый баланс 🏛", description="", color=interaction.user.color)
                    avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                    embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                    results = execute_query ("SELECT bank, inarm FROM economy WHERE userid = ?", (interaction.user.id,))
                    bank = results[0][0]
                    inarm = results[0][1]
                    total = int(bank)+int(inarm)
                    execute_query("UPDATE economy SET total = ? WHERE userid = ?", (total, interaction.user.id,))
                    embedVar.add_field(name="На руках", value=f'{inarm} <:Ametist:1042372594067832882>', inline=False)
                    embedVar.add_field(name="В банке", value=f'{bank} <:Ametist:1042372594067832882>', inline=False)
                    embedVar.add_field(name="Всего", value=f'{total} <:Ametist:1042372594067832882>', inline=False)
                    embedVar.add_field(name="📗 Инструкция", value=f"Чтобы перевести все деньги сразу, вы можете ввести вместо числа all/всё/все", inline=False)
        
                    await interaction.response.edit_message(embed=embedVar)
                else:
                    await interaction.response.send_message("Введённая вами сумма должна быть больше нуля.", ephemeral = True)
        except:
            await interaction.response.send_message("Вы вводите некорректные данные!\nПожалуйста, введите **число**, если хотите перевести часть денег в банк\nИли напиши **все**, если хотите перевести все деньги в банк", ephemeral = True)
class BalanceModalrem(discord.ui.Modal, title='Ввод суммы'):
    bot = commands.Bot
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.TextInput(label='Введите сумму, которую вывести с банка', style=discord.TextStyle.short, required=True, max_length=6))
    async def on_submit(self, interaction: discord.Interaction):
        summ_val = self.children[0].value
        try:
            results = execute_query("SELECT bank, inarm FROM economy WHERE userid = ? LIMIT 1",(interaction.user.id,))
            bank = results[0][0]
            inarm = results[0][1]
            try:
                summ_val = int(summ_val)
                if summ_val >0:
                    if summ_val <= bank:
                        newinarm = int(inarm)+int(summ_val)
                        execute_query("UPDATE economy SET inarm = ? WHERE userid = ?", (newinarm, interaction.user.id,))
                        newbank = bank-summ_val
                        execute_query("UPDATE economy SET bank = ? WHERE userid = ?", (newbank, interaction.user.id,))
                        embedVar = discord.Embed(title="Новый баланс 🏛", description="", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                        results = execute_query("SELECT bank, inarm FROM economy WHERE userid = ? LIMIT 1",(interaction.user.id,))
                        bank = results[0][0]
                        inarm = results[0][1]
                        total = int(bank)+int(inarm)
                        execute_query("UPDATE economy SET total = ? WHERE userid = ?", (total, interaction.user.id,))
                        embedVar.add_field(name="На руках", value=f'{inarm} <:Ametist:1042372594067832882>', inline=False)
                        embedVar.add_field(name="В банке", value=f'{bank} <:Ametist:1042372594067832882>', inline=False)
                        embedVar.add_field(name="Всего", value=f'{total} <:Ametist:1042372594067832882>', inline=False)
                        embedVar.add_field(name="📗 Инструкция", value=f"Чтобы перевести все деньги сразу, вы можете ввести вместо числа all/всё/все", inline=False)
        
                        await interaction.response.edit_message(embed=embedVar)
                    else:
                        embedVar = discord.Embed(title="", description="Вы указали число, превышающее количество денег в банке", color=interaction.user.color)
                        await interaction.response.send_message(embed=embedVar,ephemeral=True)
                else:
                    embedVar = discord.Embed(title="", description="Вы указали число, превышающее количество денег в банке", color=interaction.user.color)
                    await interaction.response.send_message("Введённая вами сумма должна быть больше нуля.", ephemeral = True)
            except:
                summ_val_lower = summ_val.lower()
                if summ_val_lower == "все" or summ_val_lower == "всё" or summ_val_lower == "all":
                    newinarm = int(inarm)+int(bank)
                    execute_query("UPDATE economy SET inarm = ? WHERE userid = ?", (newinarm, interaction.user.id,))
                    newbank = 0
                    execute_query("UPDATE economy SET bank = ? WHERE userid = ?", (newbank, interaction.user.id,))
                    embedVar = discord.Embed(title="Новый баланс 🏛", description="", color=interaction.user.color)
                    avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                    embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                    results = execute_query("SELECT bank, inarm FROM economy WHERE userid = ? LIMIT 1",(interaction.user.id,))
                    bank = results[0][0]
                    inarm = results[0][1]
                    total = int(bank)+int(inarm)
                    execute_query("UPDATE economy SET total = ? WHERE userid = ?", (total, interaction.user.id,))
                    embedVar.add_field(name="На руках", value=f'{inarm} <:Ametist:1042372594067832882>', inline=False)
                    embedVar.add_field(name="В банке", value=f'{bank} <:Ametist:1042372594067832882>', inline=False)
                    embedVar.add_field(name="Всего", value=f'{total} <:Ametist:1042372594067832882>', inline=False)
                    embedVar.add_field(name="📗 Инструкция", value=f"Чтобы перевести все деньги сразу, вы можете ввести вместо числа all/всё/все", inline=False)
                    await interaction.response.edit_message(embed=embedVar)
                else:
                    await interaction.response.send_message("Введённая вами сумма должна быть больше нуля.", ephemeral = True)
        except:
            await interaction.response.send_message("Вы вводите некорректные данные!\nПожалуйста, введите **число**, если хотите перевести часть денег в банк\nИли напиши **все**, если хотите перевести все деньги в банк", ephemeral = True)
class Birthday(discord.ui.Modal, title='Ввод даты рождения'):
    bot = commands.Bot

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.TextInput(label='Введите дату рождения (дд.мм.гггг)', required=True, max_length=10))

    async def on_submit(self, interaction: discord.Interaction):
        date_input = self.children[0].value
        try:
            day, month, year = map(int, date_input.split('.'))
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1960 <= year <= 2011):
                raise ValueError
            date_obj = datetime(year, month, day)
            formatted_date = date_obj.strftime('%Y-%m-%d')
            execute_query("UPDATE economy SET Birthday = ? WHERE userid = ?", (formatted_date, interaction.user.id,))
            await interaction.response.send_message(f'Вы ввели дату: {formatted_date}', ephemeral=True)
        except ValueError:
            await interaction.response.send_message('Некорректный формат даты. Пожалуйста, введите дату в формате дд.мм.гггг', ephemeral=True)

class economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):          
        global guild
        global general
        guild = self.bot.get_guild(842110386215321650)
        general = self.bot.get_channel(845009437261037678)
        execute_query("""CREATE TABLE IF NOT EXISTS economy (
            userid INT,
            inventory STR,
            bank INT,
            inarm INT,
            total INT,
            rob_command_cd DATETIME,
            work_command_cd DATETIME,
            daily_cd DATETIME,
            lottery_cd DATETIME,
            blackjack_cd DATETIME,
            fish_cd DATETIME,
            inventory_cd DATETIME,
            shop_cd DATETIME,
            trivia_cd DATETIME,
            give_cd DATETIME,
            giveitem_cd DATETIME,
            Birthday DATE,
            birthday_cd DATETIME,
            job,
            count_in_job
        )""")
        execute_query("""CREATE TABLE IF NOT EXISTS lottery (
            userid INT
        )""")
        execute_query("""CREATE TABLE IF NOT EXISTS trivia (
            id INTEGER PRIMARY KEY,
            question TEXT,
            answer1 TEXT,
            answer2 TEXT,
            answer3 TEXT,
            answer4 TEXT,
            correct_answer INTEGER,
            category_id INTEGER
        )""")
        execute_query("""CREATE TABLE IF NOT EXISTS players (
            userid INTEGER PRIMARY KEY,
            player_hand TEXT,
            player_hand_2 TEXT,
            dealer_hand TEXT,
            deck TEXT
        )""")
        execute_query("""CREATE TABLE IF NOT EXISTS profile (
            userid INT,
            marryid INT,
            i INT,
            banner_name TEXT
        )""")
        execute_query("""CREATE TABLE IF NOT EXISTS channels (
            channelid INT,
            userid INT
        )""")
        #execute_query("UPDATE economy SET count_in_job = ? WHERE userid = ? ", (50,1268425446236749886,))
        self.Birthday.start()
        print(f"eco is ready")
    @tasks.loop(seconds = 3600)
    async def Birthday(self):
        global guild
        time= datetime.now()
        if time.hour >= 10:
            current_date = datetime.now()
            yesterday_date = current_date - timedelta(days=1)
            current_month_day = current_date.strftime('%m-%d')
            yesterday_month_day = yesterday_date.strftime('%m-%d')
            results = execute_query("SELECT userid FROM economy WHERE strftime('%m-%d', Birthday) IN (?, ?)", (current_month_day, yesterday_month_day))
            birthday_role = discord.utils.get(guild.roles, id = 952934726509928500)
            for user_id in results:
                user = guild.get_member(user_id[0])
                if user:
                    birthday_date = execute_query("SELECT Birthday FROM economy WHERE userid = ?", (user_id[0],))
                    bd_date = birthday_date[0][0]
                    if birthday_date and bd_date:
                        birthday_date_obj = datetime.strptime(str(bd_date), '%Y-%m-%d').date()
                        current_date_obj = datetime.now().date()
                        birthday_month_day = birthday_date_obj.strftime('%m-%d')
                        current_month_day = current_date_obj.strftime('%m-%d')
                        if birthday_month_day == current_month_day:
                            if birthday_role not in user.roles:
                                await user.add_roles(birthday_role)
                                embedVar = discord.Embed(title="Поздравляю с днем рождения! 🎉", description="Желаю здоровья, душевного благополучия и денежного изобилия.\n Пусть твои желания будут исполнены, цели достигнуты, а проблемы решены!", color=0xff6500)
                                embedVar.add_field(name="С наилучшими пожеланиями! 🥳", value="", inline=True)
                                embedVar.add_field(name="", value="А́neko.", inline=True)
                                embedVar_2= discord.Embed(title="", description=f"### Сегодня день рождения у {user.mention}! 🥳\n Давайте все вместе поздравим этого прекрасного человека и пожелаем всего самого наилучшего!", color=0xff6500)
                                embedVar_2.add_field(name="", value="*Не забудьте надеть праздничные шапочки! 🤭*", inline=True)
                                await user.send(embed=embedVar)
                                await general.send(embed=embedVar_2)
                        elif birthday_month_day == yesterday_month_day:
                            if birthday_role in user.roles:
                                await user.remove_roles(birthday_role)
                else:
                    print(f"User with ID {user_id} not found in the server.")
    @app_commands.command(name = 'bal')
    async def _money(self, interaction: discord.Interaction):
        embedVar = discord.Embed(title="Баланс🏛", description="", color=interaction.user.color)
        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
        embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
        results =execute_query("SELECT bank, inarm FROM economy WHERE userid = ? LIMIT 1", (interaction.user.id,))
        if results:
            bank = results[0][0]
            inarm = results[0][1]
            total = int(bank)+int(inarm)
            execute_query("UPDATE economy SET total = ? WHERE userid = ?", (total, interaction.user.id,))
            embedVar.add_field(name="На руках", value=f'{inarm} <:Ametist:1042372594067832882>', inline=False)
            embedVar.add_field(name="В банке", value=f'{bank} <:Ametist:1042372594067832882>', inline=False)
            embedVar.add_field(name="Всего", value=f'{total} <:Ametist:1042372594067832882>', inline=False)
            embedVar.add_field(name="📗 Инструкция", value=f"Чтобы перевести все деньги сразу, вы можете ввести вместо числа all/всё/все", inline=False)
            view = MyView(timeout=None)
            await interaction.response.send_message(embed = embedVar, view = view,ephemeral=True)
        else:
            execute_query("""
            INSERT INTO economy (userid, bank, inarm,total)
            SELECT ?, ?, ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM economy WHERE userid = ?
            )
        """, (interaction.user.id,0,0,0,interaction.user.id))
            embedVar=discord.Embed("Вас не было в базе данных.", description="Только что вас добавило в базу данных, напишите команду ещё раз!", color=interaction.user.color)
            await interaction.response.send_message(embed = embedVar,ephemeral=True)
    @app_commands.command(name = 'rob')
    async def _rob(self, interaction: discord.Interaction, пользователь: discord.User):
        if interaction.user.id == пользователь.id:
            embedVar_3 = discord.Embed(title="❌Нельзя ограбить себя❌", description="Укажи другого пользователя", color=0xe74c3c)
            await interaction.response.send_message(embed=embedVar_3)
            return
        results =execute_query("SELECT * FROM economy WHERE userid = ? LIMIT 1", (interaction.user.id,))
        if results:
            rob_command_cd = results[0][5]
            if rob_command_cd and rob_command_cd[0] is not None and datetime.now() - datetime.strptime(rob_command_cd, '%Y-%m-%d %H:%M:%S') < timedelta(hours=14):
                last_command_time = datetime.strptime(rob_command_cd, '%Y-%m-%d %H:%M:%S')
                time_elapsed = datetime.now() - last_command_time
                remaining_time = timedelta(hours=14) - time_elapsed
                if remaining_time > timedelta():
                    hours = remaining_time.seconds // 3600
                    minutes = (remaining_time.seconds // 60) % 60
                    seconds = remaining_time.seconds % 60
                    time_message = ""
                    if hours > 0:
                        time_message += f"{hours} часов "
                    if minutes > 0:
                        time_message += f"{minutes} минут "
                    if seconds > 0:
                        time_message += f"{seconds} секунд "
                    await interaction.response.send_message(f"Подождите еще {time_message}перед следующим использованием команды.",ephemeral=True)
                    return
            chance_to_rob = random.randint(1,10)
            if chance_to_rob >5:
                if results:
                
                    results_2 =execute_query("SELECT inarm FROM economy WHERE userid = ? LIMIT 1", (пользователь.id,))
                    balance_rob = results_2[0][0]
                    balance_user = results[0][3]
                    if balance_rob>0:
                        new_user_balance = round(balance_rob/2) + balance_user
                        new_robbed_user_balance = round(balance_rob/2)
                        execute_query("UPDATE economy SET inarm = ? WHERE userid = ?", (new_user_balance, interaction.user.id,))
                        execute_query("UPDATE economy SET inarm = ? WHERE userid = ?", (new_robbed_user_balance, пользователь.id,))
                        embedVar_1 = discord.Embed(title="Кража👐", description="", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_1.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_1.add_field(name="Вы украли у ", value=f'{пользователь.mention} - {round(balance_rob/2)} <:Ametist:1042372594067832882>', inline=False)
                        embedVar = discord.Embed(title="Вас ограбили!", description=f"{interaction.user.mention} украл у вас - {balance_rob/2}<:Ametist:1042372594067832882>", color=interaction.user.color)
                        await пользователь.send(embed=embedVar)
                        await interaction.response.send_message(embed=embedVar_1)
                        execute_query("UPDATE economy SET rob_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
                    else:
                        embedVar_1 = discord.Embed(title="Кража", description="", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_1.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_1 = discord.Embed(title="", description="У пользователя нет денег", color=interaction.user.color)
                        await interaction.response.send_message(embed=embedVar_1)
                else:
                    embedVar_1 = discord.Embed(title="Ошибка при ограблении", description="пользователя нет в базе", color=interaction.user.color)
                    await interaction.response.send_message(embed=embedVar_1)
            else:
                embedVar_2 = discord.Embed(title="Неудача!", description="Вы неудачно ограбили пользователя", color=interaction.user.color)
                embedVar_2.add_field(name="У вас со счёта сняли деньги в оплату штрафа", value="Штраф в размере 250<:Ametist:1042372594067832882> был списан с вашего баланса", inline=False)
                balance_user = results[0][3]
                balance_user = balance_user - 250
                execute_query("UPDATE economy SET inarm = ? WHERE userid = ?", (balance_user, interaction.user.id,))
                execute_query("UPDATE economy SET rob_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
                await interaction.response.send_message(embed = embedVar_2)
        else:
            execute_query("""
                INSERT INTO economy (userid, bank, inarm)
                SELECT ?, ?, ?
                WHERE NOT EXISTS (
                    SELECT 1 FROM economy WHERE userid = ?
                )
            """, (interaction.user.id,0,0,interaction.user.id))
            embedVar=discord.Embed("Вас не было в базе данных.", description="Только что вас добавило в базу данных, напишите команду ещё раз!", color=interaction.user.color)
            await interaction.response.send_message(embed = embedVar,ephemeral=True)
    @app_commands.command(name = 'work',description=(f"Работать"))
    async def _work(self, interaction: discord.Interaction):
        results =execute_query("SELECT COUNT(*) FROM economy WHERE userid = ? LIMIT 1", (interaction.user.id,))
        if results[0][0] > 0:
            results =execute_query("SELECT * FROM economy WHERE userid = ? LIMIT 1", (interaction.user.id,))
            work_command_cd = results[0][6]
            if work_command_cd and work_command_cd is not None and datetime.now() - datetime.strptime(work_command_cd, '%Y-%m-%d %H:%M:%S') < timedelta(minutes=1):
                last_command_time = datetime.strptime(work_command_cd, '%Y-%m-%d %H:%M:%S')
                time_elapsed = datetime.now() - last_command_time
                remaining_time = timedelta(minutes=1) - time_elapsed
                if remaining_time > timedelta():
                    hours = remaining_time.seconds // 3600
                    minutes = (remaining_time.seconds // 60) % 60
                    seconds = remaining_time.seconds % 60
                    time_message = ""
                    if hours > 0:
                        time_message += f"{hours} часов "
                    if minutes > 0:
                        time_message += f"{minutes} минут "
                    if seconds > 0:
                        time_message += f"{seconds} секунд "
                    await interaction.response.send_message(f"Подождите еще {time_message}перед следующим использованием команды.",ephemeral=True)
                    return
            work_success = random.randint(0, 10)
            user_money_arm = results[0][3]
            job_curr = execute_query("SELECT job FROM economy WHERE userid=?",(interaction.user.id,))
            job = job_curr[0][0]
            if job =="Уборщик":
                if work_success > 2:
                    work_reward = random.randint(200,500)
                    new_balance = user_money_arm + work_reward
                    embedVar_6 = discord.Embed(title="Вы хорошо убрались!🛠", description="Вот ваша награда.", color=interaction.user.color)
                    avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                    embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                    embedVar_6.add_field(name="Вы получаете", value=f"{work_reward} <:Ametist:1042372594067832882>", inline=False)
                    await interaction.response.send_message(embed = embedVar_6)
                    execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
                else:
                    user_money_arm = results[0][3]
                    reward_fail = 200
                    new_balance =user_money_arm - reward_fail
                    embedVar_6 = discord.Embed(title="Вы перевернули мусорку!📉", description="", color=interaction.user.color)
                    avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                    embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                    embedVar_6.add_field(name="Штраф в размере - ", value="200<:Ametist:1042372594067832882> был снят с вашего баланса", inline=False)
                    await interaction.response.send_message(embed = embedVar_6)
                    execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
            elif job =="Официант":
                    if work_success > 2:
                        work_reward = random.randint(500,700)
                        new_balance = user_money_arm + work_reward
                        embedVar_6 = discord.Embed(title="Вы хорошо обслуживали клиентов!🛠", description="Вот ваша награда.", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_6.add_field(name="Вы получаете", value=f"{work_reward} <:Ametist:1042372594067832882>", inline=False)
                        await interaction.response.send_message(embed = embedVar_6)
                        execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
                    else:
                        user_money_arm = results[0][3]
                        reward_fail = 500
                        new_balance =user_money_arm - reward_fail
                        embedVar_6 = discord.Embed(title="Вы разбили тарелки!📉", description="", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_6.add_field(name="Штраф в размере - ", value="500<:Ametist:1042372594067832882> был снят с вашего баланса", inline=False)
                        await interaction.response.send_message(embed = embedVar_6)
                        execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
            elif job =="Администратор_кафе":
                    if work_success > 2:
                        work_reward = random.randint(700,1000)
                        new_balance = user_money_arm + work_reward
                        embedVar_6 = discord.Embed(title="Вы хорошо выполняли свои обязанности!🛠", description="Вот ваша награда.", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_6.add_field(name="Вы получаете", value=f"{work_reward} <:Ametist:1042372594067832882>", inline=False)
                        await interaction.response.send_message(embed = embedVar_6)
                        execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
                    else:
                        user_money_arm = results[0][3]
                        reward_fail = 700
                        new_balance =user_money_arm - reward_fail
                        embedVar_6 = discord.Embed(title="Вы ошиблись в заполнении отчёта!📉", description="", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_6.add_field(name="Штраф в размере - ", value="700<:Ametist:1042372594067832882> был снят с вашего баланса", inline=False)
                        await interaction.response.send_message(embed = embedVar_6)
                        execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
            elif job =="Менеджер_по_продажам":
                    if work_success > 2:
                        work_reward = random.randint(1000,1300)
                        new_balance = user_money_arm + work_reward
                        embedVar_6 = discord.Embed(title="Вы хорошо продавали товар!🛠", description="Вот ваша награда.", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_6.add_field(name="Вы получаете", value=f"{work_reward} <:Ametist:1042372594067832882>", inline=False)
                        await interaction.response.send_message(embed = embedVar_6)
                        execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
                    else:
                        user_money_arm = results[0][3]
                        reward_fail = 1000
                        new_balance =user_money_arm - reward_fail
                        embedVar_6 = discord.Embed(title="Вы не ничего не продали!📉", description="", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_6.add_field(name="Штраф в размере - ", value="1000<:Ametist:1042372594067832882> был снят с вашего баланса", inline=False)
                        await interaction.response.send_message(embed = embedVar_6)
                        execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
            elif job =="Специалист_по_закупкам":
                    if work_success > 2:
                        work_reward = random.randint(1300,1500)
                        new_balance = user_money_arm + work_reward
                        embedVar_6 = discord.Embed(title="Вы закупили правильный товар!🛠", description="Вот ваша награда.", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_6.add_field(name="Вы получаете", value=f"{work_reward} <:Ametist:1042372594067832882>", inline=False)
                        await interaction.response.send_message(embed = embedVar_6)
                        execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
                    else:
                        user_money_arm = results[0][3]
                        reward_fail = 1300
                        new_balance =user_money_arm - reward_fail
                        embedVar_6 = discord.Embed(title="Вы закупили не тот товар!📉", description="", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_6.add_field(name="Штраф в размере - ", value="1300<:Ametist:1042372594067832882> был снят с вашего баланса", inline=False)
                        await interaction.response.send_message(embed = embedVar_6)
                        execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
            elif job =="Менеджер_по_маркетингу":
                    if work_success > 2:
                        work_reward = random.randint(1500,2000)
                        new_balance = user_money_arm + work_reward
                        embedVar_6 = discord.Embed(title="Вы использовали правильную стратегию!🛠", description="Вот ваша награда.", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_6.add_field(name="Вы получаете", value=f"{work_reward} <:Ametist:1042372594067832882>", inline=False)
                        await interaction.response.send_message(embed = embedVar_6)
                        execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
                    else:
                        user_money_arm = results[0][3]
                        reward_fail = 1500
                        new_balance =user_money_arm - reward_fail
                        embedVar_6 = discord.Embed(title="Вы использовали неверную стратегию.!📉", description="", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_6.add_field(name="Штраф в размере - ", value="1500<:Ametist:1042372594067832882> был снят с вашего баланса", inline=False)
                        await interaction.response.send_message(embed = embedVar_6)
                        execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
            elif job =="Начальник_отдела":
                    if work_success > 2:
                        work_reward = random.randint(2000,2500)
                        new_balance = user_money_arm + work_reward
                        embedVar_6 = discord.Embed(title="Вы хорошо распределяете обязанности!🛠", description="Вот ваша награда.", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_6.add_field(name="Вы получаете", value=f"{work_reward} <:Ametist:1042372594067832882>", inline=False)
                        await interaction.response.send_message(embed = embedVar_6)
                        execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
                    else:
                        user_money_arm = results[0][3]
                        reward_fail = 2000
                        new_balance =user_money_arm - reward_fail
                        embedVar_6 = discord.Embed(title="У вас не получилось...📉", description="Вы неправильно распределили обязанности.", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_6.add_field(name="Штраф в размере - ", value="2000<:Ametist:1042372594067832882> был снят с вашего баланса", inline=False)
                        await interaction.response.send_message(embed = embedVar_6)
                        execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
            elif job =="Заместитель_директора":
                    if work_success > 2:
                        work_reward = random.randint(2500,3000)
                        new_balance = user_money_arm + work_reward
                        embedVar_6 = discord.Embed(title="Вы хорошо выполняете обязанности!🛠", description="Вот ваша награда.", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_6.add_field(name="Вы получаете", value=f"{work_reward} <:Ametist:1042372594067832882>", inline=False)
                        await interaction.response.send_message(embed = embedVar_6)
                        execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
                    else:
                        user_money_arm = results[0][3]
                        reward_fail = 2500
                        new_balance =user_money_arm - reward_fail
                        embedVar_6 = discord.Embed(title="Вы плохо выполнили поручение директора!📉", description="", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_6.add_field(name="Штраф в размере - ", value="2500<:Ametist:1042372594067832882> был снят с вашего баланса", inline=False)
                        await interaction.response.send_message(embed = embedVar_6)
                        execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
            elif job =="Директор_филиала":
                    if work_success > 2:
                        work_reward = random.randint(3000,3500)
                        new_balance = user_money_arm + work_reward
                        embedVar_6 = discord.Embed(title="Вы хорошо управляете предприятием!🛠", description="Вот ваша награда.", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_6.add_field(name="Вы получаете", value=f"{work_reward} <:Ametist:1042372594067832882>", inline=False)
                        await interaction.response.send_message(embed = embedVar_6)
                        execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
                    else:
                        user_money_arm = results[0][3]
                        reward_fail = 3000
                        new_balance =user_money_arm - reward_fail
                        embedVar_6 = discord.Embed(title="Ваши действия были неверными!📉", description="Что привело к уменьшению прибыли предприятия.", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_6.add_field(name="Штраф в размере - ", value="3000<:Ametist:1042372594067832882> был снят с вашего баланса", inline=False)
                        await interaction.response.send_message(embed = embedVar_6)
                        execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
            elif job =="Генеральный_директор_компании":
                    if work_success > 2:
                        work_reward = random.randint(3500,4000)
                        new_balance = user_money_arm + work_reward
                        embedVar_6 = discord.Embed(title="Вы хорошо выполняете свою работу!🛠", description="Вот ваша награда.", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_6.add_field(name="Вы получаете", value=f"{work_reward} <:Ametist:1042372594067832882>", inline=False)
                        await interaction.response.send_message(embed = embedVar_6)
                        execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
                    else:
                        user_money_arm = results[0][3]
                        reward_fail = 3500
                        new_balance =user_money_arm - reward_fail
                        embedVar_6 = discord.Embed(title="Вы заснули на рабочем месте!📉", description="", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                        embedVar_6.add_field(name="Штраф в размере - ", value="3500<:Ametist:1042372594067832882> был снят с вашего баланса", inline=False)
                        await interaction.response.send_message(embed = embedVar_6)
                        execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
            else:
                if work_success > 2:
                    work_reward = random.randint(50,200)
                    new_balance = user_money_arm + work_reward
                    embedVar_6 = discord.Embed(title="Вы хорошо поработали!🛠", description="Вот ваша награда.", color=interaction.user.color)
                    avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                    embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                    embedVar_6.add_field(name="Вы получаете", value=f"{work_reward} <:Ametist:1042372594067832882>", inline=False)
                    await interaction.response.send_message(embed = embedVar_6)
                    execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
                else:
                    user_money_arm = results[0][3]
                    reward_fail = 25
                    new_balance =user_money_arm - reward_fail
                    embedVar_6 = discord.Embed(title="Вы сделали брак!📉", description="", color=interaction.user.color)
                    avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                    embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                    embedVar_6.add_field(name="Штраф в размере - ", value="25<:Ametist:1042372594067832882> был снят с вашего баланса", inline=False)
                    await interaction.response.send_message(embed = embedVar_6)
                    execute_query("UPDATE economy SET work_command_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id,))
            execute_query("UPDATE economy SET inarm = ? WHERE userid = ?", (int(new_balance), interaction.user.id,))
            bank = results[0][2]
            inarm = results[0][3]
            total = int(bank)+int(inarm)
            res = execute_query("SELECT count_in_job FROM economy WHERE userid=?",(interaction.user.id,))
            res = res[0][0]
            if res:
                count = int(res)
                count +=1
                execute_query("UPDATE economy SET count_in_job = ? WHERE userid = ?", (int(count), interaction.user.id,))
                execute_query("UPDATE economy SET total = ? WHERE userid = ?", (int(total),interaction.user.id,))
            else:
                count = 1
                execute_query("UPDATE economy SET count_in_job = ? WHERE userid = ?", (int(count), interaction.user.id,))
                execute_query("UPDATE economy SET total = ? WHERE userid = ?", (int(total),interaction.user.id,))
            
        else:
            
            embedVar=discord.Embed("Вас не было в базе данных.", description="Только что вас добавило в базу данных, напишите команду ещё раз!", color=interaction.user.color)
            await interaction.response.send_message(embed=embedVar,ephemeral=True)
            execute_query("""
            INSERT INTO economy (userid, bank, inarm,count_in_job,)
            SELECT ?, ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM economy WHERE userid = ?
                )
            """, (interaction.user.id,0,0,0,interaction.user.id))
    @app_commands.command(name = 'addbalance',description=(f"Добавить денег к балансу в банке"))
    async def _addbalance(self, interaction: discord.Interaction, кому: discord.User, сколько: int):
        admin_role_id = 842301433454002187
        admin_role_id_1 = 878158525409407047
        admin_role_1 = discord.utils.get(interaction.guild.roles, id=admin_role_id_1)
        admin_role = discord.utils.get(interaction.guild.roles, id=admin_role_id)
        if admin_role in interaction.user.roles or admin_role_1 in interaction.user.roles or interaction.user.id ==323895676515909632:
            results = execute_query("SELECT * FROM economy WHERE userid = ? LIMIT 1", (кому.id,))
            user_exists = results
            if user_exists is None:
                embedVar_7 = discord.Embed(title="Ошибка при добавлении баланса", description="Пользователя не существует в базе данных", color=interaction.user.color) 
                await interaction.response.send_message(embed = embedVar_7)
                return
            else:
                if сколько > 0:
                    user_money_bank = results[0][2]
                    user_money_bank += сколько
                    embedVar_7 = discord.Embed(title="Измение баланса.", description=f"Баланс в банке у {кому.mention}\nУвеличен на {сколько}", color=interaction.user.color)   
                    await interaction.response.send_message(embed = embedVar_7)
                    execute_query("UPDATE economy SET bank = ? WHERE userid = ?", (user_money_bank, кому.id,))
                else:
                    embedVar_7 = discord.Embed(title="Указанная сумма отрицательна", description="Для уменьшения баланса пользователя используйте команду `/removebalance`", color=interaction.user.color)   
                    await interaction.response.send_message(embed = embedVar_7)
                    return
        else:
            embedVar_7 = discord.Embed(title="У вас нет доступа", description="", color=interaction.user.color)   
            await interaction.response.send_message(embed = embedVar_7)
    @app_commands.command(name = 'removebalance',description=(f"Уменьшить деньги в банке"))
    async def _removebalance(self, interaction: discord.Interaction, кому: discord.User, сколько: int):
        admin_role_id = 842301433454002187
        admin_role_id_1 = 878158525409407047
        admin_role_1 = discord.utils.get(interaction.guild.roles, id=admin_role_id_1)
        admin_role = discord.utils.get(interaction.guild.roles, id=admin_role_id)
        if admin_role in interaction.user.roles or admin_role_1 in interaction.user.roles or interaction.user.id ==323895676515909632: 
            results = execute_query("SELECT userid FROM economy WHERE userid = ? LIMIT 1", (кому.id,))
            user_exists = results
            if user_exists is None:
                embedVar_7 = discord.Embed(title="Ошибка при добавлении баланса", description="Пользователя не существует в базе данных", color=interaction.user.color) 
                await interaction.response.send_message(embed = embedVar_7)
                return
            else:
                if сколько > 0:
                    user_money_bank = results[0][2]
                    user_money_bank -= сколько
                    embedVar_7 = discord.Embed(title=" Изменение баланса ", description=f"Баланс в банке у {кому.mention} уменьшен на {сколько}", color=interaction.user.color)   
                    await interaction.response.send_message(embed = embedVar_7)
                    execute_query("UPDATE economy SET bank = ? WHERE userid = ?", (user_money_bank, кому.id,))
                else:
                    embedVar_7 = discord.Embed(title="Указанная сумма отрицательна", description="", color=interaction.user.color)   
                    await interaction.response.send_message(embed = embedVar_7)
                    return
        else:
            embedVar_7 = discord.Embed(title="У вас нет доступа", description="", color=interaction.user.color)   
            await interaction.response.send_message(embed = embedVar_7)
    @app_commands.command(name = 'daily',description=(f"Ежедневная награда"))
    async def _daily(self, interaction: discord.Interaction):
        execute_query("""
            INSERT INTO economy (userid, bank, inarm)
            SELECT ?, ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM economy WHERE userid = ?
            )
        """, (interaction.user.id,0,0,interaction.user.id))
        results = execute_query("SELECT * FROM economy WHERE userid = ? LIMIT 1", (interaction.user.id,))
        daily_cd = results[0][7]
        if daily_cd and daily_cd is not None and datetime.now() - datetime.strptime(daily_cd, '%Y-%m-%d %H:%M:%S') < timedelta(hours=24):
            last_command_time = datetime.strptime(daily_cd, '%Y-%m-%d %H:%M:%S')
            time_elapsed = datetime.now() - last_command_time
            remaining_time = timedelta(hours=24) - time_elapsed
            if remaining_time > timedelta():
                hours = remaining_time.seconds // 3600
                minutes = (remaining_time.seconds // 60) % 60
                seconds = remaining_time.seconds % 60
                time_message = ""
                if hours > 0:
                    time_message += f"{hours} часов "
                if minutes > 0:
                    time_message += f"{minutes} минут "
                if seconds > 0:
                    time_message += f"{seconds} секунд "
                await interaction.response.send_message(f"Подождите еще {time_message}перед следующим использованием команды.",ephemeral=True)
                return
        else:
            embedVar = discord.Embed(title="Вы получили ежедневную награду!🎉", description="Вам начислено 250<:Ametist:1042372594067832882>\n Возвращайтесь завтра и забирайте снова!", color=interaction.user.color)
            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
            await interaction.response.send_message(embed = embedVar)
            inarms = results[0][3]
            inarms +=250
            execute_query("UPDATE economy SET inarm = ? WHERE userid = ?",(inarms, interaction.user.id))
            execute_query("UPDATE economy SET daily_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
            bank = results[0][2]
            inarm = results[0][3]
            total = int(bank)+int(inarm)
            execute_query("UPDATE economy SET total = ? WHERE userid = ?", (int(total),interaction.user.id,))
    @app_commands.command(name = 'buylottery',description=(f"Лотерейка(100<:Ametist:1042372594067832882>"))#lottery_time
    async def _buylottery(self, interaction: discord.Interaction):
        results = execute_query("SELECT * FROM economy WHERE userid=? LIMIT 1", (interaction.user.id,))
        user_exist = results
        if user_exist is not None:
            lottery_cd = results[0][8]
            if lottery_cd and lottery_cd is not None and datetime.now() - datetime.strptime(lottery_cd, '%Y-%m-%d %H:%M:%S') < timedelta(minutes=10):
                last_command_time = datetime.strptime(lottery_cd, '%Y-%m-%d %H:%M:%S')
                time_elapsed = datetime.now() - last_command_time
                remaining_time = timedelta(minutes=10) - time_elapsed
                if remaining_time > timedelta():
                    minutes = (remaining_time.seconds // 60) % 60
                    seconds = remaining_time.seconds % 60
                    time_message = ""
                    if minutes > 0:
                        time_message += f"{minutes} минут "
                    if seconds > 0:
                        time_message += f"{seconds} секунд "
                    await interaction.response.send_message(f"Подождите еще {time_message}перед следующим использованием команды.",ephemeral=True)
                    return
            else:
                inarm = results[0][3]
                if inarm >= 100:
                    execute_query("INSERT INTO lottery (userid) VALUES (?) ",(interaction.user.id,))
                    inarm -=100
                    execute_query("UPDATE economy SET inarm=? WHERE userid=?",(inarm, interaction.user.id,))
                    execute_query("UPDATE economy SET lottery_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
                    bank = results[0][2]
                    inarm = results[0][3]
                    total = int(bank)+int(inarm)
                    execute_query("UPDATE economy SET total = ? WHERE userid = ?", (int(total),interaction.user.id,))
                    len_part = execute_query("SELECT userid FROM lottery")
                    count_participants = len(len_part)
                    embedVar = discord.Embed(title="Вы купили лотерейный билет!🎟", description=f"Начните лотерею с помощью команды `/startlottery`\n Убедитесь, что минимум 3 человека участвуют в лоттерее\nКоличество билетов, участвующих в лотерее: {count_participants}", color=interaction.user.color)
                    avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                    embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                    await interaction.response.send_message(embed=embedVar)
                else:
                    await interaction.response.send_message("У вас должно быть 100<:Ametist:1042372594067832882> на руках.")
        else:
            execute_query("""
                INSERT INTO economy (userid, bank, inarm)
                SELECT ?, ?, ?
                WHERE NOT EXISTS (
                    SELECT 1 FROM economy WHERE userid = ?
                    )
            """, (interaction.user.id,0,0,interaction.user.id))
            embedVar=discord.Embed("Вас не было в базе данных.", description="Только что вас добавило в базу данных, напишите команду ещё раз!", color=interaction.user.color)
            await interaction.response.send_message(embed=embedVar,ephemeral=True)
    @app_commands.command(name = 'startlottery',description=(f"Начинайте от 3-х человек"))
    async def _startlottery(self, interaction: discord.Interaction):
        execute_query("""
            INSERT INTO economy (userid, bank, inarm)
            SELECT ?, ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM economy WHERE userid = ?
            )
        """, (interaction.user.id,0,0,interaction.user.id))
        results = execute_query("SELECT userid FROM lottery")
        participants = results
        if participants is not None and len(participants) >= 3:
            winner = random.choice(participants) 
            winner_id = winner[0]
            results_win = execute_query("SELECT inarm FROM economy WHERE userid=? LIMIT 1", (winner_id,))
            winner_balance = results_win[0][0]
            win_dep = 100*len(participants)
            winner_balance += win_dep
            execute_query("UPDATE economy SET inarm=? WHERE userid=?", (winner_balance, winner_id))
            execute_query("DELETE FROM lottery")  
            winner_user = guild.get_member(winner_id)
            embedVar = discord.Embed(title="Итоги лотереи🎟", description=f"В лотерею выиграл(а) {winner_user.mention} приз - {win_dep}<:Ametist:1042372594067832882>", color=interaction.user.color)
            await interaction.response.send_message(embed=embedVar)
        else:
            for participant in participants:
                results_not = execute_query("SELECT * FROM economy WHERE userid=? LIMIT 1", (participant[0],))
                inarm = results_not[0][3]
                inarm += 100 
                execute_query("UPDATE economy SET inarm=? WHERE userid=?", (inarm, participant[0]))
                bank = results_not[0][2]
                inarm = results_not[0][3]
                total = int(bank)+int(inarm)
                execute_query("UPDATE economy SET total = ? WHERE userid = ?", (int(total),interaction.user.id,))
            execute_query("DELETE FROM lottery")
            embedVar = discord.Embed(title="Недостаточно игроков в лотерею", description="Деньги были возвращены на баланс тем, кто купил лотерейный билет", color=interaction.user.color)
            await interaction.response.send_message(embed=embedVar)
    @app_commands.command(name='blackjack',description=(f"Блэкджек"))
    async def _blackjack(self, interaction: discord.Interaction, ставка:int):
        global bets
        global blackVar
        execute_query("""
            INSERT INTO economy (userid, bank, inarm)
            SELECT ?, ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM economy WHERE userid = ?
            )
        """, (interaction.user.id,0,0,interaction.user.id))
        deck = [
                '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
                '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
                '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
                '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
        ]

        results = execute_query("SELECT * FROM economy WHERE userid = ? LIMIT 1", (interaction.user.id,))
        blackjack_cd = results[0][9]
        if blackjack_cd and blackjack_cd is not None and datetime.now() - datetime.strptime(blackjack_cd, '%Y-%m-%d %H:%M:%S') < timedelta(minutes=3):
            last_command_time = datetime.strptime(blackjack_cd, '%Y-%m-%d %H:%M:%S')
            time_elapsed = datetime.now() - last_command_time
            remaining_time = timedelta(minutes=3) - time_elapsed
            if remaining_time > timedelta():
                hours = remaining_time.seconds // 3600
                minutes = (remaining_time.seconds // 60) % 60
                seconds = remaining_time.seconds % 60
                time_message = ""
                if hours > 0:
                    time_message += f"{hours} часов "
                if minutes > 0:
                    time_message += f"{minutes} минут "
                if seconds > 0:
                    time_message += f"{seconds} секунд "
                await interaction.response.send_message(f"Подождите еще {time_message}перед следующим использованием команды.",ephemeral=True)
                return
        
        money_inarm = results[0][3]
        if ставка <= money_inarm and ставка > 49:
            bets = ставка
            player_hand = []
            dealer_hand = []
            player_hand.append(random.choice(deck))
            dealer_hand.append(random.choice(deck))
            player_hand.append(random.choice(deck))
            dealer_hand.append(random.choice(deck))
            player_cards = ', '.join(player_hand)
            dealer_cards = ', '.join([dealer_hand[0], 'X'])
            player_points = calculate_points(player_hand)
            player_hand_str = ', '.join(player_hand)
            dealer_hand_str = ', '.join(dealer_hand)
            for card in player_hand:
                deck.remove(card)
            for card in dealer_hand:
                deck.remove(card)
            deck_str = ', '.join(deck)
            execute_query("""INSERT INTO players (userid, player_hand, dealer_hand, deck)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(userid) DO UPDATE SET 
                player_hand = EXCLUDED.player_hand,
                dealer_hand = EXCLUDED.dealer_hand,
                deck = EXCLUDED.deck
            """, (interaction.user.id, player_hand_str, dealer_hand_str, deck_str))
            if dealer_hand[0] == '10'or dealer_hand[1] == '10':
                dealer_points = calculate_points(['10'])
            else:
                dealer_points = calculate_points(dealer_hand[0])
            if len(player_hand) == 2 and player_hand[0] == player_hand[1]:
                blackVar = discord.Embed(title="", description=f"## Блекджек 🃏\nВаши карты\n**{player_cards}** (Сумма очков - **{player_points}**)\nКарты дилера\n **{dealer_cards}** (Сумма очков - **{dealer_points}**+)\n", color=0x2f3136)
                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                blackVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                await interaction.response.send_message(embed=blackVar,view=view)
                view = BlackjackView_2(timeout=None)
                newinarms = money_inarm-ставка
                execute_query("UPDATE economy SET inarm = ? WHERE userid = ?",(newinarms,interaction.user.id,))
                execute_query("UPDATE economy SET blackjack_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
            else:
                blackVar = discord.Embed(title="", description=f"## Блекджек 🃏\nВаши карты\n**{player_cards}** (Сумма очков - **{player_points}**)\n \nКарты дилера\n **{dealer_cards}** (Сумма очков - **{dealer_points}**+)\n", color=0x2f3136)
                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                blackVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                view = BlackjackView(timeout=None)
                await interaction.response.send_message(embed=blackVar,view=view)
                newinarms = money_inarm-ставка
                execute_query("UPDATE economy SET inarm = ? WHERE userid = ?",(newinarms,interaction.user.id,))
                execute_query("UPDATE economy SET blackjack_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
        elif ставка <=49:
            embedVar = discord.Embed(title="", description="Минимальная ставка - 50", color=0x2f3136)
            await interaction.response.send_message(embed=embedVar,ephemeral=True)
        else:
            embedVar = discord.Embed(title="У вас на руках недостаточно средств", description="Снимите деньги на руки, чтобы начать игру.\n Минимальная ставка - 50", color=0x2f3136)
            await interaction.response.send_message(embed=embedVar,ephemeral=True)
    @app_commands.command(name='fish',description=(f"Рыбалка"))
    async def _fish(self, interaction: discord.Interaction):
        execute_query("""
            INSERT INTO economy (userid, bank, inarm)
            SELECT ?, ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM economy WHERE userid = ?
            )
        """, (interaction.user.id,0,0,interaction.user.id))
        results = execute_query("SELECT * FROM economy WHERE userid = ?", (interaction.user.id,))
        fish_cd = results[0][10]
        if fish_cd and fish_cd is not None and datetime.now() - datetime.strptime(fish_cd, '%Y-%m-%d %H:%M:%S') < timedelta(minutes=1):
            last_command_time = datetime.strptime(fish_cd, '%Y-%m-%d %H:%M:%S')
            time_elapsed = datetime.now() - last_command_time
            remaining_time = timedelta(minutes=1) - time_elapsed
            if remaining_time > timedelta():
                hours = remaining_time.seconds // 3600
                minutes = (remaining_time.seconds // 60) % 60
                seconds = remaining_time.seconds % 60
                time_message = ""
                if hours > 0:
                    time_message += f"{hours} часов "
                if minutes > 0:
                    time_message += f"{minutes} минут "
                if seconds > 0:
                    time_message += f"{seconds} секунд "
                await interaction.response.send_message(f"Подождите еще {time_message}перед следующим использованием команды.",ephemeral=True)
                return
        inventory_row = results[0][1]
        if inventory_row:
            inventory = inventory_row
            if inventory:
                if "Удочка" in inventory:
                    chance_fish = random.randint(1, 100)
                    if chance_fish <= 10:
                        inventory_items = inventory.split(",")
                        inventory_items.remove("Удочка")
                        inventory = ",".join(inventory_items)
                        await interaction.response.send_message("Во время рыбалки ваша удочка сломалась.")
                        execute_query("UPDATE economy SET inventory = ? WHERE userid = ?", (inventory, interaction.user.id))
                        return
                    elif chance_fish >= 95:
                        caught_fish_id =fish_list[37]
                        caught_fish_name = caught_fish_id["name"]
                        if caught_fish_name in ["Золотой ключ🔑"]:
                            if inventory_row:
                                inventory = inventory_row
                                if inventory:
                                    inventory += f",{caught_fish_name}"
                                else:
                                    inventory = caught_fish_name
                            else:
                                inventory = caught_fish_name
                            
                            embedVar = discord.Embed(title="РыбалОчка", description=f"Вы сходили на рыбалку и поймали - {caught_fish_name}\n С помощью ключа вы можете открыть кейс или продать его другим пользователям.\n`/case Легендарный`.", color=interaction.user.color)
                            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                            await interaction.response.send_message(embed=embedVar)
                            execute_query("UPDATE economy SET inventory = ? WHERE userid = ?", (inventory, interaction.user.id))
                            execute_query("UPDATE economy SET fish_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
                            return
                    elif chance_fish >= 90:
                        caught_fish_id = fish_list[36]
                        caught_fish_name = caught_fish_id["name"]
                        if caught_fish_name in ["Серебряный ключ🔑"]:
                            if inventory_row:
                                inventory = inventory_row
                                if inventory:
                                    inventory += f",{caught_fish_name}"
                                else:
                                    inventory = caught_fish_name
                            else:
                                inventory = caught_fish_name
                            
                            embedVar = discord.Embed(title="РыбалОчка", description=f"Вы сходили на рыбалку и поймали - {caught_fish_name}\n С помощью ключа вы можете открыть кейс или продать его другим пользователям.\n`/case Редкий`.", color=interaction.user.color)
                            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                            await interaction.response.send_message(embed=embedVar)
                            execute_query("UPDATE economy SET inventory = ? WHERE userid = ?", (inventory, interaction.user.id))
                            execute_query("UPDATE economy SET fish_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
                            return
                    elif chance_fish >= 80:
                        caught_fish_id = fish_list[35]
                        caught_fish_name = caught_fish_id["name"]
                        if caught_fish_name in ["Обычный ключ🔑"]:
                            if inventory_row:
                                inventory = inventory_row
                                if inventory:
                                    inventory += f",{caught_fish_name}"
                                else:
                                    inventory = caught_fish_name
                            else:
                                inventory = caught_fish_name
                            embedVar = discord.Embed(title="РыбалОчка", description=f"Вы сходили на рыбалку и поймали - {caught_fish_name}\n С помощью ключа вы можете открыть кейс или продать его другим пользователям.\n`/case Стандартный`.", color=interaction.user.color)
                            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                            await interaction.response.send_message(embed=embedVar)
                            execute_query("UPDATE economy SET inventory = ? WHERE userid = ?", (inventory, interaction.user.id))
                            execute_query("UPDATE economy SET fish_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
                            return
                    else:
                        caught_fish_id = random.choice(list(fish_list.keys()))
                        caught_fish_info = fish_list[caught_fish_id]
                        caught_fish_name = caught_fish_info["name"]
                        if caught_fish_name in ["Фугу🐡", "Окунь🐟", "Лосось🐟", "Карп🐟", "Тунец🐟", "Кит🐳","Белуга-альбинос🐠","Тигровая акула🦈","Сом🐟", "Треска🐟","Сазан🐟","Баса🐟", "Форель🐟","Морской окунь🐟", "Акула-молот🦈", "Сельдь🐟", "Морской лещ🐟", "Амур🐟", "Мускус🐟", "Карась🐟", "Бурбот🐟", "Щука🐟", "Плотва🐟", "Кольцевой коралл🌊"]:
                            if inventory_row:
                                inventory = inventory_row
                                if inventory:
                                    inventory += f",{caught_fish_name}"
                                else:
                                    inventory = caught_fish_name
                            else:
                                inventory = caught_fish_name
                            embedVar = discord.Embed(title="РыбалОчка", description=f"Вы сходили на рыбалку и поймали - {caught_fish_name}", color=interaction.user.color)
                            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                            await interaction.response.send_message(embed=embedVar)
                            execute_query("UPDATE economy SET inventory = ? WHERE userid = ?", (inventory, interaction.user.id))
                            execute_query("UPDATE economy SET fish_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
                        else:
                            
                            embedVar = discord.Embed(title="РыбалОчка", description=f"Вы сходили на рыбалку и поймали - {caught_fish_name}. Это мусор, поэтому вы ничего не получаете.", color=interaction.user.color)
                            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                            await interaction.response.send_message(embed=embedVar)
                            execute_query("UPDATE economy SET fish_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
                else:
                    await interaction.response.send_message("Для рыбалки вам нужна удочка.\n Напишите `/buy 1`",ephemeral=True)
            else:
                await interaction.response.send_message("У вас нет ничего в инвентаре. Для рыбалки вам нужна удочка.\n Напишите `/buy 1`",ephemeral=True)
        else:
            await interaction.response.send_message("У вас нет ничего в инвентаре. Для рыбалки вам нужна удочка.\n Напишите `/buy 1`",ephemeral=True)
    @app_commands.command(name='inv',description=(f"Инвентарь"))
    async def _inv(self, interaction: discord.Interaction):
        execute_query("""
            INSERT INTO economy (userid, bank, inarm)
            SELECT ?, ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM economy WHERE userid = ?
            )
        """, (interaction.user.id,0,0,interaction.user.id))
        results = execute_query("SELECT * FROM economy WHERE userid = ? LIMIT 1", (interaction.user.id,))
        inventory_cd = results[0][11]
        if inventory_cd and inventory_cd is not None and datetime.now() - datetime.strptime(inventory_cd, '%Y-%m-%d %H:%M:%S') < timedelta(seconds=20):
            last_command_time = datetime.strptime(inventory_cd, '%Y-%m-%d %H:%M:%S')
            time_elapsed = datetime.now() - last_command_time
            remaining_time = timedelta(seconds=20) - time_elapsed
            if remaining_time > timedelta():
                hours = remaining_time.seconds // 3600
                minutes = (remaining_time.seconds // 60) % 60
                seconds = remaining_time.seconds % 60
                time_message = ""
                if hours > 0:
                    time_message += f"{hours} часов "
                if minutes > 0:
                    time_message += f"{minutes} минут "
                if seconds > 0:
                    time_message += f"{seconds} секунд "
                await interaction.response.send_message(f"Подождите еще {time_message}перед следующим использованием команды.",ephemeral=True)
                return
        inventory_row = results[0][1]
        if inventory_row:
            inventory = inventory_row
            if inventory:
                items = inventory.split(",")
                item_counts = {}
                for item in items:
                    item_counts[item] = item_counts.get(item, 0) + 1
                field_value = ""
                field_value = "\n".join([f"{i+1}. {item}" for i, item in enumerate(items)])
                embedVar = discord.Embed(title=f"Инвентарь🎒", description=field_value, color=0x2f3136)
                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                execute_query("UPDATE economy SET inventory_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
                await interaction.response.send_message(embed=embedVar)
            else:
                execute_query("UPDATE economy SET inventory_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
                embedVar = discord.Embed(title="Ваш инвентарь пуст.", description="", color=0x2f3136)
                await interaction.response.send_message(embed=embedVar)
        else:
            execute_query("UPDATE economy SET inventory_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
            embedVar = discord.Embed(title="Ваш инвентарь пуст.", description="", color=0x2f3136)
            await interaction.response.send_message(embed=embedVar)
    @app_commands.command(name='shop',description=(f"Магазин"))
    async def _shop(self, interaction: discord.Interaction, страница:int):
        results = execute_query("SELECT * FROM economy WHERE userid = ?", (interaction.user.id,))
        shop_cd = results[0][12]
        if shop_cd and shop_cd is not None and datetime.now() - datetime.strptime(shop_cd, '%Y-%m-%d %H:%M:%S') < timedelta(seconds=20):
            last_command_time = datetime.strptime(shop_cd, '%Y-%m-%d %H:%M:%S')
            time_elapsed = datetime.now() - last_command_time
            remaining_time = timedelta(seconds=20) - time_elapsed
            if remaining_time > timedelta():
                hours = remaining_time.seconds // 3600
                minutes = (remaining_time.seconds // 60) % 60
                seconds = remaining_time.seconds % 60
                time_message = ""
                if hours > 0:
                    time_message += f"{hours} часов "
                if minutes > 0:
                    time_message += f"{minutes} минут "
                if seconds > 0:
                    time_message += f"{seconds} секунд "
                await interaction.response.send_message(f"Подождите еще {time_message}перед следующим использованием команды.",ephemeral=True)
                return
        if страница ==1:
            embedVar = discord.Embed(title="Магазин 🛒", description="Доступные предметы для покупки:", color=discord.Color.blue())
            for item_id, item_info in shop_items.items():
                if item_id <15:
                    if 'id' in item_info:
                        role_id = item_info['id']
                        role = discord.utils.get(interaction.guild.roles, id=role_id)
                        if role:
                            embedVar.add_field(name=f"", value=f"{item_id}. <@&{role_id}>\nЦена: {item_info['price']} <:Ametist:1042372594067832882>", inline=False)
                        else:
                            item_name = item_info['name']
                    else:
                        item_name = item_info['name']
                        embedVar.add_field(name=f"", value=f"**{item_id}. {item_name}**Цена: {item_info['price']} <:Ametist:1042372594067832882>", inline=False)
            
            await interaction.response.send_message(embed=embedVar)
            execute_query("UPDATE economy SET shop_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
        elif страница ==2:
            embedVar = discord.Embed(title="Магазин 🛒", description="Доступные предметы для покупки:", color=discord.Color.blue())
            for item_id, item_info in shop_items.items():
                if item_id >=15 and item_id <= 30:
                    if 'id' in item_info:
                        role_id = item_info['id']
                        role = discord.utils.get(interaction.guild.roles, id=role_id)
                        if role:
                            embedVar.add_field(name=f"", value=f"{item_id}. <@&{role_id}>\nЦена: {item_info['price']} <:Ametist:1042372594067832882>", inline=False)
                        else:
                            item_name = item_info['name']
                    else:
                        item_name = item_info['name']
                        embedVar.add_field(name=f"", value=f"**{item_id}. {item_name}**Цена: {item_info['price']} <:Ametist:1042372594067832882>", inline=False)
            
            await interaction.response.send_message(embed=embedVar)
            execute_query("UPDATE economy SET shop_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
        elif страница ==3:
            embedVar = discord.Embed(title="Магазин 🛒", description="Доступные предметы для покупки:", color=discord.Color.blue())
            for item_id, item_info in shop_items.items():
                if item_id >30:
                    if 'id' in item_info:
                        role_id = item_info['id']
                        role = discord.utils.get(interaction.guild.roles, id=role_id)
                        if role:
                            embedVar.add_field(name=f"", value=f"{item_id}. <@&{role_id}>\nЦена: {item_info['price']} <:Ametist:1042372594067832882>", inline=False)
                        else:
                            item_name = item_info['name']
                    else:
                        item_name = item_info['name']
                        embedVar.add_field(name=f"", value=f"**{item_id}. {item_name}**Цена: {item_info['price']} <:Ametist:1042372594067832882>", inline=False)
            await interaction.response.send_message(embed=embedVar)
            execute_query("UPDATE economy SET shop_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
        else:
            await interaction.response.send_message("В магазине всего 3 страницы, используйте `/shop 1,2,3`",ephemeral=True)
    @app_commands.command(name='buy',description=(f"Купить"))
    async def _buy(self, interaction: discord.Interaction,предмет:int):
        execute_query("""
            INSERT INTO economy (userid, bank, inarm)
            SELECT ?, ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM economy WHERE userid = ?
            )
        """, (interaction.user.id,0,0,interaction.user.id))
        results = execute_query("SELECT * FROM economy WHERE userid=?",(interaction.user.id,))
        inarmmoney = results[0][3]
        if предмет in shop_items:
            item_info = shop_items[предмет]
            if inarmmoney >= item_info['price']:
                inventory_row = results[0][1]
                if inventory_row:
                    inventory = inventory_row
                    if inventory:
                        inventory_items = inventory.split(",")
                    else:
                        inventory_items = []
                    if item_info['name'] not in inventory_items:
                        if inventory:
                            inventory += f",{item_info['name']}"
                        else:
                            inventory = item_info['name']
                        execute_query("UPDATE economy SET inventory = ? WHERE userid = ?", (inventory, interaction.user.id))
                        inarmmoney -= item_info['price']
                        execute_query("UPDATE economy SET inarm = ? WHERE userid = ?", (inarmmoney, interaction.user.id))
                        await interaction.response.send_message(f"Вы купили💰 {item_info['name']} за {item_info['price']} <:Ametist:1042372594067832882>",ephemeral=True)
                    else:
                        await interaction.response.send_message("У вас уже есть этот предмет в инвентаре.",ephemeral=True)
                else:
                    inventory = item_info['name']
                    execute_query("UPDATE economy SET inventory = ? WHERE userid = ?", (inventory, interaction.user.id))
                    inarmmoney -= item_info['price']
                    execute_query("UPDATE economy SET inarm = ? WHERE userid = ?", (inarmmoney, interaction.user.id))
                    await interaction.response.send_message(f"Вы купили💰 {item_info['name']} за {item_info['price']} <:Ametist:1042372594067832882>",ephemeral=True)
            else:
                await interaction.response.send_message("У вас недостаточно монет для покупки этого предмета.",ephemeral=True)
        else:
            await interaction.response.send_message("Такого предмета нет в магазине.",ephemeral=True)
    @app_commands.command(name='sell',description=(f"Продать"))
    async def _sell(self, interaction: discord.Interaction,предмет:int):
        execute_query("""
            INSERT INTO economy (userid, bank, inarm)
            SELECT ?, ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM economy WHERE userid = ?
            )
        """, (interaction.user.id,0,0,interaction.user.id))
        results = execute_query("SELECT * FROM economy WHERE userid=?",(interaction.user.id,))
        inarmmoney = results[0][3]
        inventory_row = results[0][1]
        if inventory_row:
            inventory_items = inventory_row.split(",") 
            if предмет <= len(inventory_items):
                item_to_sell = inventory_items[предмет-1]
                for shop_item in shop_items.values():
                    if shop_item["name"] == item_to_sell:
                        item_info = shop_item
                        inventory_items.remove(item_to_sell)
                        inventory = ",".join(inventory_items)
                        execute_query("UPDATE economy SET inventory = ? WHERE userid = ?", (inventory, interaction.user.id))
                        inarmmoney += item_info['price']
                        execute_query("UPDATE economy SET inarm = ? WHERE userid = ?", (inarmmoney, interaction.user.id))
                        embedVar = discord.Embed(title="", description=f"Вы продали🔄 {item_info['name']} за {item_info['price']} <:Ametist:1042372594067832882>", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                        bank = results[0][2]
                        inarm = results[0][3]
                        total = int(bank)+int(inarm)
                        execute_query("UPDATE economy SET total = ? WHERE userid = ?", (int(total),interaction.user.id,))
                        await interaction.response.send_message(embed=embedVar)
                        return
                for fish_lists in fish_list.values():
                    if fish_lists["name"]==item_to_sell:
                        item_info = fish_lists
                        inventory_items.remove(item_to_sell)
                        inventory = ",".join(inventory_items)
                        execute_query("UPDATE economy SET inventory = ? WHERE userid = ?", (inventory, interaction.user.id))
                        inarmmoney += item_info['price']
                        execute_query("UPDATE economy SET inarm = ? WHERE userid = ?", (inarmmoney, interaction.user.id))
                        embedVar = discord.Embed(title="", description=f"Вы продали🔄 {item_info['name']} за {item_info['price']} <:Ametist:1042372594067832882>", color=interaction.user.color)
                        avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                        embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                        bank = results[0][2]
                        inarm = results[0][3]
                        total = int(bank)+int(inarm)
                        execute_query("UPDATE economy SET total = ? WHERE userid = ?", (int(total),interaction.user.id,))
                        await interaction.response.send_message(embed=embedVar)
                        return
            else:
                await interaction.response.send_message("Неверный номер предмета.", ephemeral=True)
        else:
            await interaction.response.send_message("У вас нет ничего в инвентаре.",ephemeral=True)
    @app_commands.command(name='give',description=(f"Передать деньги"))
    async def _give(self, interaction: discord.Interaction,кому: discord.User,сколько:int):
        execute_query("""
            INSERT INTO economy (userid, bank, inarm)
            SELECT ?, ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM economy WHERE userid = ?
            )
        """, (interaction.user.id,0,0,interaction.user.id))
        results = execute_query("SELECT * FROM economy WHERE userid = ?", (interaction.user.id,))
        give_cd = results[0][14]
        if give_cd and give_cd is not None and datetime.now() - datetime.strptime(give_cd, '%Y-%m-%d %H:%M:%S') < timedelta(minutes=1):
            last_command_time = datetime.strptime(give_cd, '%Y-%m-%d %H:%M:%S')
            time_elapsed = datetime.now() - last_command_time
            remaining_time = timedelta(minutes=1) - time_elapsed
            if remaining_time > timedelta():
                hours = remaining_time.seconds // 3600
                minutes = (remaining_time.seconds // 60) % 60
                seconds = remaining_time.seconds % 60
                time_message = ""
                if hours > 0:
                    time_message += f"{hours} часов "
                if minutes > 0:
                    time_message += f"{minutes} минут "
                if seconds > 0:
                    time_message += f"{seconds} секунд "
                await interaction.response.send_message(f"Подождите еще {time_message}перед следующим использованием команды.",ephemeral=True)
                return
        results_2 = execute_query("SELECT * FROM economy WHERE userid=?",(кому.id,))
        user_accept = results_2[0][0]
        if interaction.user.id !=кому:
            if user_accept:
                moneys = results[0][3]
                if сколько > moneys:
                    await interaction.response.send_message(f"У вас недостаточно средств на руках")
                    return
                if сколько > 0:
                    moneys_2 = results_2[0][3]
                    moneys_2 +=сколько
                    
                    embedVar = discord.Embed(title="Вы успешно передали деньги!💲", description=f"Пользователю - {кому.mention}\n В размере - {сколько}<:Ametist:1042372594067832882>", color=0x2f3136)
                    embedVar2 = discord.Embed(title="Вам передали деньги!💲", description=f"{interaction.user.mention} в размере - {сколько}<:Ametist:1042372594067832882>", color=0x2f3136)
                    avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                    embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                    avatar_url = кому.avatar.url if кому.avatar.url else None
                    embedVar2.set_author(name=кому.name, icon_url=avatar_url)
                    await кому.send(embed=embedVar2)
                    await interaction.response.send_message(embed=embedVar,ephemeral=True)
                    execute_query("UPDATE economy SET inarm=? WHERE userid=?",(moneys_2,кому.id,))
                    moneys -=сколько
                    execute_query("UPDATE economy SET inarm=? WHERE userid=?",(moneys,interaction.user.id,))
                    execute_query("UPDATE economy SET give_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
                else:
                    embedVar = discord.Embed(title="Неверно указана сумма", description=f"Вы указали отрицательное число.", color=interaction.user.color)
                    await interaction.response.send_message(embed=embedVar,ephemeral=True)
            else:
                await interaction.response.send_message(f"Пользователя не существует в базе данных.",ephemeral=True)
        else:
            await interaction.response.send_message(f"Вы не можете передать деньги себе.",ephemeral=True)
    @app_commands.command(name='use',description=(f"Использовать предмет из инвентаря"))
    async def _use(self, interaction: discord.Interaction,предмет: int):
        execute_query("""
            INSERT INTO economy (userid, bank, inarm)
            SELECT ?, ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM economy WHERE userid = ?
            )
        """, (interaction.user.id,0,0,interaction.user.id))
        global guild
        user = interaction.user
        results = execute_query("SELECT inventory FROM economy WHERE userid = ?", (interaction.user.id,))
        inventory_row = results[0][0]
        item_index = предмет
        if inventory_row:
            inventory = inventory_row.split(",")
        
            if 0 < item_index <= len(inventory):
                item_to_use = inventory[item_index - 1]
                for shop_item in shop_items.values():
                    if shop_item["name"] == item_to_use:
                        item_info = shop_item
                        if item_info and 'id' in item_info:
                            role_id = item_info['id']
                            role = discord.utils.get(guild.roles,id = role_id)
                            if role:
                                if not role in user.roles:
                                    inventory.remove(item_to_use)
                                    inventory = ",".join(inventory)
                                    execute_query("UPDATE economy SET inventory = ? WHERE userid = ?", (inventory, interaction.user.id))
                                    await user.add_roles(role,reason="",atomic=True)
                                    embedVar = discord.Embed(title="", description=f"Вы успешно получили роль <@&{role_id}>!", color=role.color)
                                    avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                                    embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                                    await interaction.response.send_message(embed=embedVar,ephemeral=True)
                                    return
                                elif role in user.roles:
                                    embedVar = discord.Embed(title="", description=f"У вас уже есть эта роль, вы можете её продать или передать другому.", color=interaction.user.color)
                                    avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                                    embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                                    await interaction.response.send_message(embed=embedVar,ephemeral=True)
                                    return
                            else:
                                embedVar = discord.Embed(title="", description=f"Этот предмет не является ролью на сервере.", color=interaction.user.color)
                                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                                embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                                await interaction.response.send_message(embed=embedVar,ephemeral=True)
                                return 
                        elif item_to_use =="Удочка":
                            embedVar = discord.Embed(title="", description=f"Чтобы использовать удочку, напишите `/fish`", color=interaction.user.color)
                            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                            embedVar.set_author(name=interaction.user.name, icon_url=avatar_url)
                            await interaction.response.send_message(embed=embedVar,ephemeral=True)
                            return
  
            else:
                await interaction.response.send_message("Некорректный номер предмета. Проверьте ваш инвентарь.",ephemeral=True)
        else:
            await interaction.response.send_message("У вас нет предметов в инвентаре.",ephemeral=True)
    @app_commands.command(name='giveitem',description=(f"Передать предмет"))
    async def _giveitem(self, interaction: discord.Interaction, кому: discord.User, предмет: int):
        execute_query("""
            INSERT INTO economy (userid, bank, inarm)
            SELECT ?, ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM economy WHERE userid = ?
            )
        """, (interaction.user.id,0,0,interaction.user.id))
        results = execute_query("SELECT * FROM economy WHERE userid = ?", (кому.id,))
        user_accept = results[0][0]
        results_2 = execute_query("SELECT * FROM economy WHERE userid = ?", (interaction.user.id,))
        giveitem_cd = results_2[0][15]
        if giveitem_cd and giveitem_cd is not None and datetime.now() - datetime.strptime(giveitem_cd, '%Y-%m-%d %H:%M:%S') < timedelta(minutes=1):
            last_command_time = datetime.strptime(giveitem_cd, '%Y-%m-%d %H:%M:%S')
            time_elapsed = datetime.now() - last_command_time
            remaining_time = timedelta(minutes=1) - time_elapsed
            if remaining_time > timedelta():
                hours = remaining_time.seconds // 3600
                minutes = (remaining_time.seconds // 60) % 60
                seconds = remaining_time.seconds % 60
                time_message = ""
                if hours > 0:
                    time_message += f"{hours} часов "
                if minutes > 0:
                    time_message += f"{minutes} минут "
                if seconds > 0:
                    time_message += f"{seconds} секунд "
                await interaction.response.send_message(f"Подождите еще {time_message}перед следующим использованием команды.",ephemeral=True)
                return
        
        if interaction.user.id != кому.id:
            if user_accept:
                inventory_row = results_2[0][1]
        
                if inventory_row:
                    inventory = inventory_row.split(",")
                    if 0 < предмет <= len(inventory):
                        item_to_give = inventory[предмет - 1]
                        inventory.remove(item_to_give)
                        new_inventory = ",".join(inventory)
                        
                        receiver_inventory_row = results[0][1]
                        if receiver_inventory_row:
                            receiver_inventory = receiver_inventory_row
                            if receiver_inventory:
                                receiver_inventory += f",{item_to_give}"
                            else:
                                receiver_inventory = item_to_give
                        else:
                            receiver_inventory = item_to_give
                        
                        embedVar = discord.Embed(title="Вам передали предмет! 📦", description=f" {item_to_give} - от {interaction.user.mention}.", color=interaction.user.color)
                        await interaction.response.send_message(кому.mention, embed=embedVar)
                        execute_query("UPDATE economy SET inventory = ? WHERE userid = ?", (new_inventory, interaction.user.id))
                        execute_query("UPDATE economy SET inventory = ? WHERE userid = ?", (receiver_inventory, кому.id))
                        execute_query("UPDATE economy SET giveitem_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
                        return
                    else:
                        await interaction.response.send_message("Некорректный номер предмета. Проверьте ваш инвентарь.",ephemeral=True)
                else:
                    await interaction.response.send_message("У вас нет предметов в инвентаре.",ephemeral=True)
            else:
                await interaction.response.send_message("Пользователя не существует в базе данных.",ephemeral=True)
        else:
            await interaction.response.send_message("Вы не можете передать предмет себе.",ephemeral=True)
    @app_commands.command(name='trivia',description=(f"Тривия"))
    async def _trivia(self, interaction: discord.Interaction):
        execute_query("""
            INSERT INTO economy (userid, bank, inarm)
            SELECT ?, ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM economy WHERE userid = ?
            )
        """, (interaction.user.id,0,0,interaction.user.id))
        results = execute_query("SELECT * FROM economy WHERE userid = ?", (interaction.user.id,))
        trivia_cd = results[0][13]
        if trivia_cd and trivia_cd is not None and datetime.now() - datetime.strptime(trivia_cd, '%Y-%m-%d %H:%M:%S') < timedelta(minutes=2):
            last_command_time = datetime.strptime(trivia_cd, '%Y-%m-%d %H:%M:%S')
            time_elapsed = datetime.now() - last_command_time
            remaining_time = timedelta(minutes=2) - time_elapsed
            if remaining_time > timedelta():
                hours = remaining_time.seconds // 3600
                minutes = (remaining_time.seconds // 60) % 60
                seconds = remaining_time.seconds % 60
                time_message = ""
                if hours > 0:
                    time_message += f"{hours} часов "
                if minutes > 0:
                    time_message += f"{minutes} минут "
                if seconds > 0:
                    time_message += f"{seconds} секунд "
                await interaction.response.send_message(f"Подождите еще {time_message}перед следующим использованием команды.",ephemeral=True)
                return
        embedVar = discord.Embed(title="Игра - тривиа 🎓", description="Тривиа - это игра, в которой вам будут задаваться вопросы из различных категорий, и вам нужно будет выбирать правильные ответы из предложенных вариантов.", color=discord.Color.blue())
        embedVar.add_field(name="Категории:", value="1. География 🌍\n2. Математика 🔢\n3. Физика 🌡\n4. Химия 💧\n5. Интернет 🌐\n6. Аниме 🍜\n7. Спорт ⚽\n8. Фильмы 🎞\n9. Музыка 🎵\n10. Автомобили 🚘", inline=False)
        view = triviaView(timeout=None)
        execute_query("UPDATE economy SET trivia_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
        await interaction.response.send_message(embed=embedVar,view=view,ephemeral=True)
    @app_commands.command(name='help',description=(f"Команды"))
    async def _help(self, interaction: discord.Interaction):
        execute_query("""
            INSERT INTO economy (userid, bank, inarm)
            SELECT ?, ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM economy WHERE userid = ?
            )
        """, (interaction.user.id,0,0,interaction.user.id))
        embedVar=discord.Embed(title="Помощь по командам.", description="`/911` - команда для экстренного упоминания модераторов\n`/utility help` - небольшая брошюрка о сервере\n**Экономика**\n`/bal` - покажет информацию о вашем балансе.\n`/inventory` - информация о вашем инвентаре.\n`/shop` - магазин, в котором можно купить роли/предметы.\n`/daily` - ежедневная награда в виде валюты.\n`/rob` - команда кражи, позволяет вам украсть деньги с рук у другого пользователя\n`/buy 1` - этой командой вы можете купить любой предмет в магазине(вместо 1 - любой номер предмета в магазине)\n`/sell` - позволяет продать предметы из инвентаря\n`/give` - передать деньги другому\n`/giveitem` - передать предмет из вашего инвентаря другому человеку\n`/work` - работа для заработка валюты\n`/fish` - ловите рыбу и продавайте её(не забудьте купить удочку в магазине)\n`/trivia` - отвечайте на вопросы правильно, и получите награду в виде валюты!\n`/lottery` покупайте лотерейные билетики и выигрывайте!\n`/startlottery` - Начните лотерею, чтобы узнать, кто победил(лотерея начинается от 3-х человек)\n`/blackjack` - Блэкджек, всё зависит от вашей удачи и умений(казино)\n `/lb` - таблица лидер по балансу(всего)\n `/lb_arm` - таблица лидер по балансу(на руках)\n`/lb_bank` - таблица лидер по балансу(в банке)\n**Действия**\n`/bite` - укусить\n`/blush` - смущаться\n`/cry` - плакать\n`/cuddle` - прижаться\n`/hug` - обнять\n`/lick` - лизнуть\n`/nom` - съесть\n`/pat` - погладить\n`/poke` - потыкать\n`/punch` - ударить\n`/slap` - дать пощёчину\n`/stare` - смотреть\n`/tickle` - щекотать\n`/profile` - профиль\n`/shop_profile` - магазин фонов профиля\n`/marry` - Пожениться/Выйти замуж\n`/divorce` - развестись\n",color =interaction.user.color)
        await interaction.response.send_message(embed=embedVar, ephemeral=True)
    @app_commands.command(name='lb')
    async def _lb(self, interaction: discord.Interaction):
        results = execute_query("SELECT userid, total FROM economy ORDER BY total DESC LIMIT 10")
        lb_data = results
        field_value = ""
        embed = discord.Embed(title="", color=0x2f3136)
        embed.set_author(name = "Топ сервера (всего) 📜", icon_url = guild.icon.url)
        for index, (userid, total) in enumerate(lb_data, start=1):
            user = self.bot.get_user(userid)
            if user:
                if index == 1:
                    field_value += f"{lb[index-1]}│{user.mention} - `{total}`<:Ametist:1042372594067832882>\n"
                elif index == 2:
                    field_value += f"{lb[index-1]}│{user.mention} - `{total}`<:Ametist:1042372594067832882>\n"
                elif index == 3:
                    field_value += f"{lb[index-1]}│{user.mention} - `{total}`<:Ametist:1042372594067832882>\n"
                elif index <=10:
                    field_value += f"{lb[index-1]}│{user.mention} - `{total}`<:Ametist:1042372594067832882>\n"
                else:
                    return
            else:
                field_value += f"{lb[index-1]}│{userid} - `{total}`<:Ametist:1042372594067832882>\n"
        embed.add_field(name=f"", value=field_value, inline=True)
        await interaction.response.send_message(embed=embed)
    @app_commands.command(name='lb_arm')
    async def _lb_arm(self, interaction: discord.Interaction):
        results = execute_query("SELECT userid, inarm FROM economy ORDER BY inarm DESC LIMIT 10")
        lb_data = results
        field_value = ""
        embed = discord.Embed(title="", color=0x2f3136)
        embed.set_author(name = "Топ сервера (на руках) 📜", icon_url = guild.icon.url)
        for index, (userid, total) in enumerate(lb_data, start=1):
            user = self.bot.get_user(userid)
            if user:
                if index == 1:
                    field_value += f"{lb[index-1]}│{user.mention} - `{total}`<:Ametist:1042372594067832882>\n"
                elif index == 2:
                    field_value += f"{lb[index-1]}│{user.mention} - `{total}`<:Ametist:1042372594067832882>\n"
                elif index == 3:
                    field_value += f"{lb[index-1]}│{user.mention} - `{total}`<:Ametist:1042372594067832882>\n"
                elif index <=10:
                    field_value += f"{lb[index-1]}│{user.mention} - `{total}`<:Ametist:1042372594067832882>\n"
                else:
                    return
            else:
                field_value += f"{lb[index-1]}│{userid} - `{total}`<:Ametist:1042372594067832882>\n"
        embed.add_field(name=f"", value=field_value, inline=True)
        await interaction.response.send_message(embed=embed)
    @app_commands.command(name='lb_bank')
    async def _lb_bank(self, interaction: discord.Interaction):
        results = execute_query("SELECT userid, bank FROM economy ORDER BY bank DESC LIMIT 10")
        lb_data = results
        field_value = ""
        embed = discord.Embed(title="", color=0x2f3136)
        embed.set_author(name = "Топ сервера (в банке) 📜", icon_url = guild.icon.url)
        for index, (userid, total) in enumerate(lb_data, start=1):
            user = self.bot.get_user(userid)
            if user:
                if index == 1:
                    field_value += f"{lb[index-1]}│{user.mention} - `{total}`<:Ametist:1042372594067832882>\n"
                elif index == 2:
                    field_value += f"{lb[index-1]}│{user.mention} - `{total}`<:Ametist:1042372594067832882>\n"
                elif index == 3:
                    field_value += f"{lb[index-1]}│{user.mention} - `{total}`<:Ametist:1042372594067832882>\n"
                elif index <=10:
                    field_value += f"{lb[index-1]}│{user.mention} - `{total}`<:Ametist:1042372594067832882>\n"
                else:
                    return
            else:
                field_value += f"{lb[index-1]}│{userid} - `{total}`<:Ametist:1042372594067832882>\n"
        embed.add_field(name=f"", value=field_value, inline=True)
        await interaction.response.send_message(embed=embed)
    @app_commands.command(name='birthday',description=(f"Укажите свой день рождения!"))
    async def _birthday(self, interaction: discord.Interaction):
        execute_query("""
            INSERT INTO economy (userid, bank, inarm)
            SELECT ?, ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM economy WHERE userid = ?
            )
        """, (interaction.user.id,0,0,interaction.user.id))
        results = execute_query("SELECT * FROM economy WHERE userid = ? LIMIT 1", (interaction.user.id,))
        birthday_cd = results[0][17]
        if birthday_cd and birthday_cd is not None and datetime.now() - datetime.strptime(birthday_cd, '%Y-%m-%d %H:%M:%S') < timedelta(hours =744):
            last_command_time = datetime.strptime(birthday_cd, '%Y-%m-%d %H:%M:%S')
            time_elapsed = datetime.now() - last_command_time
            remaining_time = timedelta(hours =744) - time_elapsed
            if remaining_time > timedelta():
                days = remaining_time.days
                hours = remaining_time.seconds // 3600
                minutes = (remaining_time.seconds // 60) % 60
                seconds = remaining_time.seconds % 60
                time_message = ""
                if days > 0:
                    time_message += f"{days} дней "
                if hours > 0:
                    time_message += f"{hours} часов "
                if minutes > 0:
                    time_message += f"{minutes} минут "
                if seconds > 0:
                    time_message += f"{seconds} секунд "
                await interaction.response.send_message(f"Подождите еще {time_message}перед следующим использованием команды.",ephemeral=True)
                return
        #execute_query("UPDATE economy SET birthday_cd = ? WHERE userid = ?", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), interaction.user.id))
        await interaction.response.send_modal(Birthday())
    @app_commands.command(name='case',description=(f"Открывайте кейсы и получайте награду(если у вас есть ключи)"))
    async def _case(self, interaction: discord.Interaction, выбор_кейса:cases):
        results = execute_query("SELECT inarm FROM economy WHERE userid = ? LIMIT 1", (interaction.user.id,))
        results_2 = execute_query("SELECT inventory FROM economy WHERE userid = ? AND (inventory LIKE ? OR inventory LIKE ? OR inventory LIKE ?) LIMIT 1",(interaction.user.id,"%Обычный ключ🔑%", "%Серебряный ключ🔑%", "%Золотой ключ🔑%",))
        if results_2:
            user_money_arm = results[0][0]
            inventory_keys = results_2[0][0]
            if inventory_keys:
                if выбор_кейса =="Стандартный":
                
                    results_2 = execute_query("SELECT inventory FROM economy WHERE userid = ? LIMIT 1", (interaction.user.id,))
                    if results_2:
                        inventory_row = results_2[0][0]
                        if "Обычный ключ🔑" in inventory_row:
                            inventory_items = inventory_row.split(",")
                            inventory_items.remove("Обычный ключ🔑")
                            inventory_updated = ",".join(inventory_items)
            
                            
                            case_reward = random.randint(50, 300)
                            new_balance = user_money_arm + case_reward
                            embedVar_6 = discord.Embed(title="Вы открыли обычный кейс!🎁", description="Вот ваша награда.", color=interaction.user.color)
                            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                            embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                            embedVar_6.add_field(name="Вы получаете", value=f"{case_reward} <:Ametist:1042372594067832882>", inline=False)
                            
                            results_3 = execute_query("SELECT bank, inarm FROM economy WHERE userid = ? LIMIT 1", (interaction.user.id,))
                            bank = results_3[0][0]
                            inarm = results_3[0][1]
                            total = int(bank)+int(inarm)
                            execute_query("UPDATE economy SET inarm = ? WHERE userid = ?", (new_balance, interaction.user.id,))
                            execute_query("UPDATE economy SET inventory = ? WHERE userid = ?", (inventory_updated, interaction.user.id))
                            execute_query("UPDATE economy SET total = ? WHERE userid = ?", (int(total),interaction.user.id,))
                        else:
                            await interaction.response.send_message(f"У вас нет обычного ключа. Рыбачьте дальше!")
                    else:
                        await interaction.response.send_message(f"У вас нет обычного ключа. Рыбачьте дальше!")
                elif выбор_кейса =="Редкий":
                    results_2 = execute_query("SELECT inventory FROM economy WHERE userid = ? LIMIT 1", (interaction.user.id,))
                    if results_2:
                        inventory_row = results_2[0][0]
                        if "Серебряный ключ🔑" in inventory_row:
                            inventory_items = inventory_row.split(",")
                            inventory_items.remove("Серебряный ключ🔑")
                            inventory_updated = ",".join(inventory_items)
            
                            
                            case_reward = random.randint(300, 500)
                            new_balance = user_money_arm + case_reward
                            embedVar_6 = discord.Embed(title="Вы открыли редкий кейс!🎁", description="Вот ваша награда.", color=interaction.user.color)
                            avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                            embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                            embedVar_6.add_field(name="Вы получаете", value=f"{case_reward} <:Ametist:1042372594067832882>", inline=False)
                            
                            results_3 = execute_query("SELECT bank, inarm FROM economy WHERE userid = ? LIMIT 1", (interaction.user.id,))
                            bank = results_3[0][0]
                            inarm = results_3[0][1]
                            total = int(bank)+int(inarm)
                            execute_query("UPDATE economy SET inarm = ? WHERE userid = ?", (new_balance, interaction.user.id,))
                            execute_query("UPDATE economy SET inventory = ? WHERE userid = ?", (inventory_updated, interaction.user.id))
                            execute_query("UPDATE economy SET total = ? WHERE userid = ?", (int(total),interaction.user.id,))
                        else:
                            await interaction.response.send_message(f"У вас нет серебряного ключа. Рыбачьте дальше!")
                    else:
                        await interaction.response.send_message(f"У вас нет серебряного ключа. Рыбачьте дальше!")
                elif выбор_кейса == "Легендарный":
                    results_2 = execute_query("SELECT inventory FROM economy WHERE userid = ? LIMIT 1", (interaction.user.id,))
                    if results_2:
                        inventory_row = results_2[0][0]
                        
                        if "Золотой ключ🔑" in inventory_row:
                            inventory_items = inventory_row.split(",")
                            inventory_items.remove("Золотой ключ🔑")
                            inventory_updated = ",".join(inventory_items)
                            execute_query("UPDATE economy SET inventory = ? WHERE userid = ?", (inventory_updated, interaction.user.id))
                            chance_on_role = random.randint(1,10000)
                            if chance_on_role >9970:
                                shop_items_filtered = {key: value for key, value in shop_items.items() if key != 1}
                                item_names = [value["name"] for value in shop_items_filtered.values()]
                                rolegive = random.choice(item_names)
                                if inventory_row:
                                    inventory = inventory_row
                                    if inventory:
                                        inventory += f",{rolegive}"
                                    else:
                                        inventory = rolegive
                                else:
                                    inventory = rolegive
                                execute_query("UPDATE economy SET inventory = ? WHERE userid = ?", (inventory, interaction.user.id))
                                embedVar_6 = discord.Embed(title="Вы открыли легендарный кейс!🎁", description="Вот ваша награда.", color=interaction.user.color)
                                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                                embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                                embedVar_6.add_field(name="Вы получаете", value=f"{rolegive}", inline=False)
                            else:
                                case_reward = random.randint(500, 1000)
                                new_balance = user_money_arm + case_reward
                                embedVar_6 = discord.Embed(title="Вы открыли легендарный кейс!🎁", description="Вот ваша награда.", color=interaction.user.color)
                                avatar_url = interaction.user.avatar.url if interaction.user.avatar else None
                                embedVar_6.set_author(name=interaction.user.name, icon_url=avatar_url)
                                embedVar_6.add_field(name="Вы получаете", value=f"{case_reward} <:Ametist:1042372594067832882>", inline=False)
                                execute_query("UPDATE economy SET inarm = ? WHERE userid = ?", (new_balance, interaction.user.id,))
                                results_3 = execute_query("SELECT bank, inarm FROM economy WHERE userid = ? LIMIT 1", (interaction.user.id,))
                                bank = results_3[0][0]
                                inarm = results_3[0][1]
                                total = int(bank)+int(inarm)
                                execute_query("UPDATE economy SET total = ? WHERE userid = ?", (int(total),interaction.user.id,))
                        else:
                            await interaction.response.send_message(f"У вас нет золотого ключа. Рыбачьте дальше!")
                    else:
                        await interaction.response.send_message(f"У вас нет золотого ключа. Рыбачьте дальше!")
            
                
                await interaction.response.send_message(embed=embedVar_6)
            else:
                await interaction.response.send_message(f"У вас нет ключей",ephemeral=True)
        else:
                await interaction.response.send_message(f"У вас нет ключей",ephemeral=True)
    @app_commands.command(name='work_choice',description=(f"Меняйте место работы, чтобы зарабатывать больше!"))
    async def _work_choice(self, interaction: discord.Interaction, выбор_работы:jobs):
        current_job = execute_query("SELECT job FROM economy WHERE userid = ?", (interaction.user.id,))
        current_job = current_job[0][0] if current_job else None
        job_hierarchy = [
            "Уборщик", "Официант", "Администратор_кафе", "Менеджер_по_продажам",
            "Специалист_по_закупкам", "Менеджер_по_маркетингу", "Начальник_отдела",
            "Заместитель_директора", "Директор_филиала", "Генеральный_директор_компании"]
        if not current_job:
            if job_hierarchy.index(выбор_работы.value) == 0:
                result = execute_query("SELECT count_in_job FROM economy WHERE userid = ?", (interaction.user.id,))
                result = result[0][0] if result else 0
                if result >= 250:
                    job = str(выбор_работы)
                    start = 5
                    stop = len(job)
                    slice_object = slice(start, stop)
                    job_1 = job[slice_object]
                    job = job_1.replace("_", " ")
                    embedVar = discord.Embed(title="Вы сменили место работы!🔁", description=f"Вы устроились на работу - {job}", color=interaction.user.color)
                    await interaction.response.send_message(embed=embedVar, ephemeral=True)
                    execute_query("UPDATE economy SET count_in_job=? WHERE userid=?", (0, interaction.user.id,))
                    execute_query("UPDATE economy SET job = ? WHERE userid = ?", (job_1, interaction.user.id))
                else:
                    skolko = 250 - result
                    if skolko >= 0:
                        embedVar = discord.Embed(title="Вам нужно больше работать!", description=f"Вы не можете сменить место работы, для этого вам нужно поработать еще {skolko} раз(а).", color=interaction.user.color)
                        await interaction.response.send_message(embed=embedVar, ephemeral=True)
                    else:
                        lens = len(job_hierarchy)
                        if job_hierarchy.index(current_job) + 1 > lens:
                            next_job_index = job_hierarchy.index(current_job)
                            next_job = job_hierarchy[next_job_index].replace("_", " ")
                            next_job = job_hierarchy[next_job_index].replace("'", "")
                            embedVar = discord.Embed(title="Вы уже можете сменить работу!", description=f"Вы можете сменить работу только на {next_job}", color=interaction.user.color)
                            await interaction.response.send_message(embed=embedVar, ephemeral=True)
                        else:
                            next_job_index = job_hierarchy.index(current_job)+1
                            next_job = job_hierarchy[next_job_index].replace("_", " ")
                            next_job = job_hierarchy[next_job_index].replace("'", "")
                            embedVar = discord.Embed(title="Вы уже можете сменить работу!", description=f"Вы можете сменить работу только на {next_job}", color=interaction.user.color)
                            await interaction.response.send_message(embed=embedVar, ephemeral=True)
            else:
                embedVar = discord.Embed(title="Нет смысла менять работу!", description=f"Для того чтобы работать '{выбор_работы.value}', вам сначала нужно поработать на '{job_hierarchy[0]}'.", color=interaction.user.color)
                await interaction.response.send_message(embed=embedVar, ephemeral=True)
        else:
            if not current_job or job_hierarchy.index(выбор_работы.value) == job_hierarchy.index(current_job)+1:
                result = execute_query("SELECT count_in_job FROM economy WHERE userid = ?", (interaction.user.id,))
                result = result[0][0] if result else 0
                if result >= 250:
                    job = str(выбор_работы)
                    start = 5
                    stop = len(job)
                    slice_object = slice(start, stop)
                    job_1 = job[slice_object]
                    job = job_1.replace("_", " ")
                    embedVar = discord.Embed(title="Вы сменили место работы!🔁", description=f"Вы устроились на работу - {job}", color=interaction.user.color)
                    await interaction.response.send_message(embed=embedVar, ephemeral=True)
                    execute_query("UPDATE economy SET count_in_job=? WHERE userid=?",(0,interaction.user.id,))
                    execute_query("UPDATE economy SET job = ? WHERE userid = ?", (job_1, interaction.user.id,))
                else:
                    skolko = 250 - result
                    if skolko >=0:
                        embedVar = discord.Embed(title="Вам нужно больше работать!", description=f"Вы не можете сменить место работы, для этого вам нужно поработать еще {skolko} раз(а).", color=interaction.user.color)
                        await interaction.response.send_message(embed=embedVar, ephemeral=True)
                    else:
                        lens = len(job_hierarchy)
                        if job_hierarchy.index(current_job) + 1 > lens:
                            next_job_index = job_hierarchy.index(current_job)
                            next_job = job_hierarchy[next_job_index].replace("_", " ")
                            next_job = job_hierarchy[next_job_index].replace("'", "")
                            embedVar = discord.Embed(title="Вы уже можете сменить работу!", description=f"Вы можете сменить работу только на {next_job}", color=interaction.user.color)
                            await interaction.response.send_message(embed=embedVar, ephemeral=True)
                        else:
                            next_job_index = job_hierarchy.index(current_job)+1
                            next_job = job_hierarchy[next_job_index].replace("_", " ")
                            next_job = job_hierarchy[next_job_index].replace("'", "")
                            embedVar = discord.Embed(title="Вы уже можете сменить работу!", description=f"Вы можете сменить работу только на {next_job}", color=interaction.user.color)
                            await interaction.response.send_message(embed=embedVar, ephemeral=True)
            else:
                next_job_index = job_hierarchy.index(current_job) + 1
                next_job = job_hierarchy[next_job_index].replace("_", " ")
                next_job = job_hierarchy[next_job_index].replace("'", "")
                job = str(выбор_работы)
                start = 5
                stop = len(job)
                slice_object = slice(start, stop)
                job_1 = job[slice_object]
                job = job_1.replace("_", " ")
                if выбор_работы.value in job_hierarchy and job_hierarchy.index(выбор_работы.value) < job_hierarchy.index(current_job):
                    embedVar = discord.Embed(title="Нет смысла менять работу!", description=f"Работа '{job}' ниже вашего текущего уровня. Это может привести к уменьшению вашего заработка.", color=interaction.user.color)
                else:
                    job = str(выбор_работы)
                    start = 5
                    stop = len(job)
                    slice_object = slice(start, stop)
                    job_1 = job[slice_object]
                    job = job_1.replace("_", " ")
                    embedVar = discord.Embed(title="Вы не можете сменить место работы!", description=f"Для того чтобы работать {job}, сначала вам нужно поработать '{next_job}'.", color=interaction.user.color)
                await interaction.response.send_message(embed=embedVar, ephemeral=True)
async def setup(bot):
    await bot.add_cog(economy(bot))