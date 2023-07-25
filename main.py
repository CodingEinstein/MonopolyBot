import telebot
from telebot import types
import roll_dice_system as DICE
import random

bot = telebot.TeleBot("6066347084:AAGd4EF5XIdluOLxFeXla-erVSziyDig8lo")


@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_message(message.chat.id, "Hello!")


@bot.message_handler(commands=["give_dice"])
def give_dice(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    btnDice = types.InlineKeyboardButton(text="Give me a Dice!", callback_data="1")
    markup.add(btnDice)
    bot.send_message(message.chat.id, "Ok, I give you dices!", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def bot_roll_dice(call):
    if call.data == "1":
        n1 = int(random.uniform(1, 7))
        n2 = int(random.uniform(1, 7))
        result = DICE.call(n1, n2, "dice1.jpg", "dice2.jpg")
        result.show()
        bot.send_photo(call.message.chat.id, result)
        bot.send_message(call.message.chat.id, "You rolled dice!")
    else:
        pass


bot.polling(none_stop=True)
