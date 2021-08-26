import telebot
#import logging
from telebot import types
from func import chat_log

#TOKEN = '1945274113:AAEYimj6dtgvk6QfNyNu8XzIhbn3dLY7koo'
CHAT_ID = '1939761627'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_english = types.InlineKeyboardButton(text='English 🇺🇸', url='https://instagram.com/coworkingifgzp?utm_medium=copy_link')
    item_español = types.InlineKeyboardButton(text='Español 🇪🇸', url='https://instagram.com/coworkingifgzp?utm_medium=copy_link')
    markup_inline.add(item_english, item_español)
    bot.send_message(message.chat.id, 'Welcome!!! Please select your language\nBienvenido!!!Por favor seleccionar un lenguaje',
                     reply_markup=markup_inline
                     )
#@bot.message_handler(regexp=)

bot.polling()

