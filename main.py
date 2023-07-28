""""" Import modules """""
import random
import time
import telebot
from telebot import types
import roll_dice_system as DICE
import user_class as char
from PIL import Image

player_name = None


def create_user(new_username, new_index, number1, number2):
    new_user = char.User(new_username, 1500, 0, 0, 0, 0, 0, new_index, number1, number2)
    return new_user



b2_n1 = int()
b2_n2 = int()
b3_n1 = int()
b3_n2 = int()
bot = telebot.TeleBot("6066347084:AAGd4EF5XIdluOLxFeXla-erVSziyDig8lo")
player_current_place = 0
current_moving_player = 1
bot_nickname_list = ['skilla', 'Lizab', 'Evnomiy', 'shmekk', 'Detrax', 'Longer', 'Blendamed', 'MonDoRiN', 'markboy',
                     'TOGORqg', 'Serocco', 'Kalkin90', 'ElleKtro', 'GlaDOS', 'OoAnid', 'DesantTS', 'Raierover', 'Yli',
                     'Cilyia', 'Heoli', 'Giel']
bot_exist_nickname_list = []
user_setup_scores = {}
user_list = []

player = create_user("", 1, 0, 0)
player.player_result = Image.new('RGB', (2160, 1440))
player.player_points_to_move = int()
player.n1 = int()
player.dice_number1 = player.n1
player.n2 = int()
player.dice_number2 = player.n2
player.points_to_move = int()
bot1 = create_user(random.choice(bot_nickname_list), 2, 0, 0)
bot1.n1 = int()
bot1.dice_number1 = bot1.n1
bot1.n2 = int()
bot1.dice_number2 = bot1.n2
bot1.points_to_move = int()
bot1.bot1_result = Image.new('RGB', (2160, 1440))
bot2 = create_user(random.choice(bot_nickname_list), 3, b2_n1, b2_n2)
bot3 = create_user(random.choice(bot_nickname_list), 4, b3_n1, b3_n2)
chat_id = None
call_chat_id = None
human_username = None
b1_result = Image.new('RGB', (2160, 1440))
b2_result = Image
b3_result = Image

b2_points_to_move = int()
b3_points_to_move = int()


@bot.message_handler(commands=['start'])
def start_game(message):
    player.nickname = f"{message.from_user.username}"
    bot.send_message(message.chat.id, "Ok, let`s start the game!")
    user_list.append(player.nickname)
    user_list.append(bot1.nickname)
    user_list.append(bot2.nickname)
    user_list.append(bot3.nickname)
    for i in user_list:
        bot.send_message(message.chat.id, f"Player: {i}")
    """"" Ready room """""
    markup = types.InlineKeyboardMarkup()
    readybtn = types.InlineKeyboardButton(text="Start Game", callback_data="ready")
    markup.add(readybtn)
    bot.send_message(message.chat.id, "All players are ready! Press 'Start Game' button to start the game!",
                     reply_markup=markup)


""""" Setup """""


@bot.callback_query_handler(func=lambda call: True)
def setup(call):
    if call.data == "ready":
        bot.send_message(call.message.chat.id, "SETUP!")
        bot.send_message(call.message.chat.id, f"The player with number {player.user_index} is rolling dices!")
        give_dice(call.message)
    elif call.data == "Roll Dice":
        player.n1 = int(random.uniform(1, 7))
        player.n2 = int(random.uniform(1, 7))
        player.player_result = DICE.call_merge(player.n1, player.n2)
        player.points_to_move = DICE.call_num(player.n1, player.n2)
        bot.send_photo(call.message.chat.id, player.player_result)
        bot.send_message(call.message.chat.id, f"You rolled dice! You got {player.points_to_move} points!")
    elif call.data == "Roll Dice Setup":
        player.n1 = int(random.uniform(1, 7))
        player.n2 = int(random.uniform(1, 7))
        player.player_result = DICE.call_merge(player.n1, player.n2)
        player.points_to_move = player.n1 + player.n2
        bot.send_photo(call.message.chat.id, player.player_result)
        bot.send_message(call.message.chat.id, f"You rolled dice! You got {player.points_to_move} points!")
        user_setup_scores.update({1: player.points_to_move})
        time.sleep(2)
        bot.send_message(call.message.chat.id, f"The player with number {bot1.user_index} is rolling dices!")
        time.sleep(2)
        bot1.b1_n1 = int(random.uniform(1, 7))
        bot1.b1_n2 = int(random.uniform(1, 7))
        bot1.bot1_result = DICE.call_num(bot1.n1, bot1.n2)
        bot1.points_to_move = bot1.n1 + bot1.n2
        bot.send_photo(call.message.chat.id, bot1.bot1_result)
        bot.send_message(call.message.chat.id, f"{bot1.nickname} rolled dice! He got {bot1.points_to_move} points!")
        user_setup_scores.update({2: bot1.points_to_move})
        time.sleep(2)
        global bot2
        bot.send_message(call.message.chat.id, f"The player with number {bot2.user_index} is rolling dices!")
        time.sleep(2)
        global b2_n1
        b2_n1 = int(random.uniform(1, 7))
        global b2_n2
        b2_n2 = int(random.uniform(1, 7))
        global b2_points_to_move
        b2_points_to_move = b2_n1 + b2_n2
        global b2_result
        b2_result = DICE.call_merge(b2_n1, b2_n2)
        bot.send_photo(call.message.chat.id, b2_result)
        bot.send_message(call.message.chat.id, f"{bot2.nickname} rolled dice! He got {b2_points_to_move} points!")
        user_setup_scores.update({3: b2_points_to_move})
        time.sleep(2)
        global bot3
        bot.send_message(call.message.chat.id, f"The player with number {bot3.user_index} is rolling dices!")
        time.sleep(2)
        global b3_n1
        b3_n1 = int(random.uniform(1, 7))
        global b3_n2
        b3_n2 = int(random.uniform(1, 7))
        global b3_points_to_move
        b3_points_to_move = b3_n1 + b3_n2
        global b3_result
        b3_result = DICE.call_merge(b3_n1, b3_n2)
        bot.send_photo(call.message.chat.id, b3_result)
        bot.send_message(call.message.chat.id, f"{bot3.nickname} rolled dice! He got {b3_points_to_move} points!")
        user_setup_scores.update({4: b3_points_to_move})
        final_dict = dict(max(user_setup_scores.items()))
        final_dict.update(dict(min(user_setup_scores.items())))
        bot.send_message(call.message.chat.id, final_dict)


@bot.message_handler(commands=["give_dice"])
def give_dice(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    btn_dice = types.InlineKeyboardButton(text="Make Move", callback_data="Roll Dice Setup")
    markup.add(btn_dice)
    bot.send_message(message.chat.id, "Take dices!", reply_markup=markup)


def give_dice_setup(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    btn_dice = types.InlineKeyboardButton(text="Make Move", callback_data="Roll Dice Setup")
    markup.add(btn_dice)
    bot.send_message(message.chat.id, "Take dices!", reply_markup=markup)


# None stop active
bot.polling(none_stop=True)

# def user_move(current_points, points_move):
# move_full = current_points + points_move
# return move_full
