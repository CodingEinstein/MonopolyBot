""""" Import modules """""
import random

import telebot
from telebot import types
import roll_dice_system as DICE
import user_class as char

bot = telebot.TeleBot("6066347084:AAGd4EF5XIdluOLxFeXla-erVSziyDig8lo")
player_current_place = 0
current_moving_player = 0
bot_nickname_list = ['skilla', 'Lizab', 'Evnomiy', 'shmekk', 'Detrax', 'Longer', 'Blendamed', 'MonDoRiN', 'markboy',
                     'TOGORqg', 'Serocco', 'Kalkin90', 'ElleKtro', 'GlaDOS', 'OoAnid', 'DesantTS']


@bot.message_handler(commands=['start'])
def start_game(message):
    bot.send_message(message.chat.id, "Ok, let`s start the game!")
    player = char.User(f"{message.from_user.username}", 1500, 0, 0, 0, 0, 0)
    bot1 = char.User(f"{random.shuffle(bot_nickname_list)}", 1500, 0, 0, 0, 0, 0)
    bot2 = char.User(f"{random.shuffle(bot_nickname_list)}", 1500, 0, 0, 0, 0, 0)
    bot3 = char.User(f"{random.shuffle(bot_nickname_list)}", 1500, 0, 0, 0, 0, 0)
    give_player(player)
    give_bot1(bot1)
    give_bot2(bot2)
    give_bot3(bot3)
    bot.send_message(message.chat.id, f"{player.nickname}, {bot1.nickname}, {bot2.nickname}, {bot3.nickname}")


def give_player(new_player):
    player = new_player
    player = return_player(player)


def give_bot1(new_bot1):
    bot1 = new_bot1
    bot1 = return_bot1(bot1)


def give_bot2(new_bot2):
    bot2 = new_bot2
    bot2 = return_bot2(bot2)


def give_bot3(new_bot3):
    bot3 = new_bot3
    bot3 = return_bot3(bot3)


def return_player(player):
    return player


def return_bot1(bot1):
    return bot1


def return_bot2(bot2):
    return bot2


def return_bot3(bot3):
    return bot3


@bot.message_handler(commands=["give_dice"])
def give_dice(message: types.Message):
    if current_moving_player == 0:
        markup = types.InlineKeyboardMarkup()
        btn_dice = types.InlineKeyboardButton(text="Make Move", callback_data="1")
        markup.add(btn_dice)
        bot.send_message(message.chat.id, "Take dices!", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def player_make_move(call):
    if call.data == "1":
        n1 = int(random.uniform(1, 7))
        n2 = int(random.uniform(1, 7))
        result = DICE.call_merge(n1, n2)
        points_to_move = DICE.call_num(n1, n2)
        bot.send_photo(call.message.chat.id, result)
        bot.send_message(call.message.chat.id, f"You rolled dice! You got {points_to_move} points!")


# None stop active
bot.polling(none_stop=True)


def user_move(current_points, points_move):
    move_full = current_points + points_move
    return move_full
