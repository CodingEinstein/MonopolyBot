""""" Import modules """""
import telebot
from telebot import types
import roll_dice_system as DICE

bot = telebot.TeleBot("6066347084:AAGd4EF5XIdluOLxFeXla-erVSziyDig8lo")


@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_message(message.chat.id, "Hello!")


@bot.message_handler(commands=["give_dice"])
def give_dice(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    btn_dice = types.InlineKeyboardButton(text="Make Move", callback_data="1")
    markup.add(btn_dice)
    bot.send_message(message.chat.id, "Ok, I give you dices!", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def bot_roll_dice(call):
    if call.data == "1":
        bot.send_photo(call.message.chat.id, DICE.call())
        bot.send_message(call.message.chat.id, "You rolled dice!")


# None stop active
bot.polling(none_stop=True)
