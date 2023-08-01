""""" Import modules """""
import random
import time
import telebot
from telebot import types
import roll_dice_system as DICE
import user_class as char
import operator
from PIL import Image

player_name = None


def create_user(new_username, new_index, number1, number2, new_image_result, points_to_move):
    new_user = char.User(new_username, 1500, 0, 0, 0, 0, 0, new_index, number1, number2, new_image_result,
                         points_to_move)
    return new_user


bot = telebot.TeleBot("6066347084:AAGd4EF5XIdluOLxFeXla-erVSziyDig8lo")
player_current_place = 0
current_moving_player = 1
bot_nickname_list = ['skilla', 'Lizab', 'Evnomiy', 'shmekk', 'Detrax', 'Longer', 'Blendamed', 'MonDoRiN', 'markboy',
                     'TOGORqg', 'Serocco', 'Kalkin90', 'ElleKtro', 'GlaDOS', 'OoAnid', 'DesantTS', 'Raierover', 'Yli',
                     'Cilyia', 'Heoli', 'Giel']
bot_exist_nickname_list = []
user_setup_scores = {}
user_startup_list = []

player = create_user("", 1, 0, 0, None, int())
player.player_result = Image.new('RGB', (2160, 1440))
player.image_result = player.player_result
player.n1 = int()
player.dice_number1 = player.n1
player.n2 = int()
player.dice_number2 = player.n2
bot1 = create_user(random.choice(bot_nickname_list), 2, 0, 0, None, int())
bot_last_name = bot1.nickname
bot1.n1 = int()
bot1.dice_number1 = bot1.n1
bot1.n2 = int()
bot1.dice_number2 = bot1.n2
bot1.bot1_result = Image
bot1.image_result = bot1.bot1_result
bot2 = create_user(bot_last_name, 3, 0, 0, None, int())
while bot2.nickname == bot_last_name:
    bot2.nickname = str(random.choice(bot_nickname_list))
    if bot2.nickname != bot_last_name:
        break
bot2.n1 = int()
bot2.dice_number1 = bot2.n1
bot2.n2 = int()
bot2.dice_number2 = bot2.n2
bot2.bot2_result = Image.new('RGB', (2160, 1440))
bot2.image_result = bot2.bot2_result
bot3 = create_user(bot_last_name, 4, 0, 0, None, int())
while bot3.nickname == bot_last_name:
    bot3.nickname = str(random.choice(bot_nickname_list))
    if bot3.nickname != bot_last_name:
        break
bot3.n1 = int()
bot3.dice_number1 = bot3.n1
bot3.n2 = int()
bot3.dice_number2 = bot3.n2
bot3.bot3_result = Image.new('RGB', (2160, 1440))
bot3.image_result = bot3.bot3_result
chat_id = None
call_chat_id = None
human_username = None


@bot.message_handler(commands=['start'])
def start_game(message):
    player.nickname = f"{message.from_user.username}"
    bot.send_message(message.chat.id, "Ok, let`s start the game!")
    user_startup_list.append(player.nickname)
    user_startup_list.append(bot1.nickname)
    user_startup_list.append(bot2.nickname)
    user_startup_list.append(bot3.nickname)
    for i in user_startup_list:
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
        def user_move_num1():
            dice_number1 = int(random.uniform(1, 7))
            return dice_number1

        def user_move_num2():
            dice_number2 = int(random.uniform(1, 7))
            return dice_number2

        def user_move_points(number1, number2):
            points_to_move = number1 + number2
            return points_to_move

        def user_move_image(number1, number2):
            image_result = DICE.call_merge(number1, number2)
            return image_result

        def user_move_send(image_result, points_to_move, nickname):
            bot.send_photo(call.message.chat.id, image_result)
            bot.send_message(call.message.chat.id, f"You rolled dice! You got {points_to_move} points!")
            user_setup_scores.update({f"{nickname}": points_to_move})
        player.n1 = user_move_num1()
        player.n2 = user_move_num2()
        player.points_to_move = user_move_points(player.n1, player.n2)
        player.image_result = user_move_image(player.n1, player.n2)
        user_move_send(player.image_result, player.points_to_move, player.nickname)
        time.sleep(2)
        bot.send_message(call.message.chat.id, f"The player with number {bot1.user_index} is rolling dices!")
        time.sleep(2)
        bot1.n1 = user_move_num1()
        bot1.n2 = user_move_num2()
        bot1.points_to_move = user_move_points(bot1.n1, bot1.n2)
        bot1.image_result = user_move_image(bot1.n1, bot1.n2)
        user_move_send(bot1.image_result, bot1.points_to_move, bot1.nickname)
        time.sleep(2)
        bot.send_message(call.message.chat.id, f"The player with number {bot2.user_index} is rolling dices!")
        time.sleep(2)
        bot2.n1 = user_move_num1()
        bot2.n2 = user_move_num2()
        bot2.points_to_move = user_move_points(bot2.n1, bot2.n2)
        bot2.image_result = user_move_image(bot2.n1, bot2.n2)
        user_move_send(bot2.image_result, bot2.points_to_move, bot2.nickname)
        time.sleep(2)
        bot.send_message(call.message.chat.id, f"The player with number {bot3.user_index} is rolling dices!")
        time.sleep(2)
        bot3.n1 = user_move_num1()
        bot3.n2 = user_move_num2()
        bot3.points_to_move = user_move_points(bot3.n1, bot3.n2)
        bot3.image_result = user_move_image(bot3.n1, bot3.n2)
        user_move_send(bot3.image_result, bot3.points_to_move, bot3.nickname)
        user_dict = sorted(user_setup_scores.items(), key=operator.itemgetter(1))
        user_dict.reverse()
        print(user_dict)
        bot.send_message(call.message.chat.id, "So, let`s see, who`s  moves first!")
        bot.send_message(call.message.chat.id, f"{user_dict}")


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
