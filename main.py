from random import random, randint

import telebot
from telebot import types

Token = "7933603125:AAFMJSowD5WECqsgfR9D2SRIVUuQVkyBO9M"

bot = telebot.TeleBot(Token)

random_list = [0, 1]
markup = types.InlineKeyboardMarkup()
bt1 = types.InlineKeyboardButton('Кинуть монетку', callback_data="drop")
@bot.message_handler(commands=['start'])
def start(message):
    markup.row(bt1)
    file = open('./image/orel.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    bot.send_message(message.chat.id, 'Привет, это бот "Орел и Решка"',reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'drop':
        random_drop = random_list[randint(0, 1)]
        if random_drop == 0:
            file_drop_orel = open('./image/dropOrel.jpg', 'rb')
            bot.send_photo(callback.message.chat.id, file_drop_orel)
            bot.send_message(callback.message.chat.id, 'Тебе выпал орел!', reply_markup=markup)
        if random_drop == 1:
            file_drop_reska = open('./image/reshka.jpg', 'rb')
            bot.send_photo(callback.message.chat.id, file_drop_reska)
            bot.send_message(callback.message.chat.id, 'Тебе выпала решка!', reply_markup=markup)
bot.polling(non_stop=True)