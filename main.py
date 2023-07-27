""""" Import modules """""
import random
import time
import telebot
from telebot import types
import roll_dice_system as DICE
import user_class as char

bot = telebot.TeleBot("6066347084:AAGd4EF5XIdluOLxFeXla-erVSziyDig8lo")
player_current_place = 0
current_moving_player = 0
bot_nickname_list = ['skilla', 'Lizab', 'Evnomiy', 'shmekk', 'Detrax', 'Longer', 'Blendamed', 'MonDoRiN', 'markboy',
                     'TOGORqg', 'Serocco', 'Kalkin90', 'ElleKtro', 'GlaDOS', 'OoAnid', 'DesantTS', 'Raierover', 'Yli',
                     'Cilyia', 'Heoli', 'Giel']
bot_exist_nickname_list = []
user_setup_scores = []
user_list = []
player = None
bot1 = None
bot2 = None
bot3 = None
player_points_to_move = None
chat_id = None
call_chat_id = None
human_username = None
@bot.message_handler(commands=['start'])
def start_game(message):
    global chat_id
    chat_id = message.chat.id
    global human_username
    human_username = message.from_user.username
    bot.send_message(chat_id, "Ok, let`s start the game!")
    global player
    player = create_user(human_username, 1)
    global bot1
    bot1 = create_user(random.choice(bot_nickname_list), 2)
    global bot2
    bot2 = create_user(random.choice(bot_nickname_list), 3)
    global bot3
    bot3 = create_user(random.choice(bot_nickname_list),  4)
    user_list.append(player.nickname)
    user_list.append(bot1.nickname)
    user_list.append(bot2.nickname)
    user_list.append(bot3.nickname)
    for i in user_list:
        bot.send_message(chat_id, f"Player: {i}")
    """"" Ready room """""
    markup = types.InlineKeyboardMarkup()
    readybtn = types.InlineKeyboardButton(text="Start Game", callback_data="ready")
    markup.add(readybtn)
    bot.send_message(message.chat.id, "All players are ready! Press 'Start Game' button to start the game!",
                     reply_markup=markup)


def create_user(new_username, new_index):
    new_user = char.User(new_username, 1500, 0, 0, 0, 0, 0, new_index)
    return new_user


""""" Setup """""


@bot.callback_query_handler(func=lambda call: True)
def setup(call, move_type):
    global call_chat_id
    call_chat_id = call.message.chat.id
    if call.data == "ready":
        bot.send_message(call_chat_id, "SETUP!")
        bot.send_message(call_chat_id, f"The player with number {player.user_index} is rolling dices!")
        give_dice(call.message)
    elif call.data == "Roll Dice":
        n1 = int(random.uniform(1, 7))
        n2 = int(random.uniform(1, 7))
        result = DICE.call_merge(n1, n2)
        player_points_to_move = DICE.call_num(n1, n2)
        bot.send_photo(call.message.chat.id, result)
        bot.send_message(call.message.chat.id, f"You rolled dice! You got {player_points_to_move} points!")
        user_setup_scores.append(player_points_to_move)




@bot.message_handler(commands=["give_dice"])
def give_dice(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    btn_dice = types.InlineKeyboardButton(text="Make Move", callback_data="Roll Dice")
    markup.add(btn_dice)
    bot.send_message(chat_id, "Take dices!", reply_markup=markup)


# None stop active
bot.polling(none_stop=True)


def user_move(current_points, points_move):
    move_full = current_points + points_move
    return move_full
