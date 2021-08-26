import telebot
#import logging
from telebot import types
#from func import chat_log

TOKEN = '1945274113:AAEYimj6dtgvk6QfNyNu8XzIhbn3dLY7koo'
CHAT_ID = '1939761627'
bot = telebot.TeleBot(TOKEN)
option = {
    "lenguage":{
        "es":{
            "label":'Español 🇪🇸',
            "option": [{
                "slug":"osint",
                "name":"OSINT"

            }]
        },
        "en":{
            "label":'English 🇺🇸',
            "option": [{
                "slug":"osint",
                "name":"OSINT"

            }]
        }
    }
}
va = option["lenguage"]
print(len(va))




markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) 
for key, value in va.items():
    ju = types.KeyboardButton(va[key]['label'])
    markup.add(ju)

#item_english = types.KeyboardButton('English 🇺🇸')
#item_español = types.KeyboardButton('Español 🇪🇸')
#markup.add(item_english, item_español)

@bot.message_handler(commands=['start', 'help'])
def start_command(message):
    bot.send_message(message.chat.id, 'Welcome!!! Please select your language\nBienvenido!!!Por favor seleccionar un lenguaje',
                     reply_markup=markup
                     )
@bot.message_handler(regexp= 'English 🇺🇸')
def item_english(message):
    #print(message.chat)
    menu_english = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    tools_osint_english = types.KeyboardButton('OSINT')
    version_pro_english = types.KeyboardButton('Version Pro')
    tools_extras_english = types.KeyboardButton('Extras')
    teams_english = types.KeyboardButton('Teams')
    help_english= types.KeyboardButton('Help')

    menu_english.add(tools_osint_english, version_pro_english, tools_extras_english, teams_english, help_english )
    bot.send_message(message.chat.id, 'Main menu\nselect an option', reply_markup= menu_english)

    @bot.message_handler(regexp='OSINT')
    def tools_osint_english(message):
        menu_osint = types.ReplyKeyboardMarkup(resize_keyboard=True)
        opt1=types.KeyboardButton('Opción 1')
        opt2=types.KeyboardButton('Opción 2')
        opt3=types.KeyboardButton('Opción 3')
        opt4=types.KeyboardButton('Opción 4')
        opt5=types.KeyboardButton('Opción 5')
        opt6=types.KeyboardButton('Main menu')
        menu_osint.add(opt1, opt2, opt3, opt4, opt5, opt6)
        bot.send_message(message.chat.id, 'Menu OSINT\nSelect an option',reply_markup=menu_osint)

        @bot.message_handler(regexp='Main menu')
        def opt6(message):
            bot.send_message(message.chat.id, 'Main menu\nselect an option', reply_markup=menu_english)
        
@bot.message_handler(regexp= 'Español 🇪🇸')
def item_español(message):
    menu_español = types.ReplyKeyboardMarkup(resize_keyboard=True)
    tools_osint= types.KeyboardButton('OSINT')
    version_pro= types.KeyboardButton('Versión Pro')
    tools_extras= types.KeyboardButton('Extras')
    teams = types.KeyboardButton('Teams')
    help= types.KeyboardButton('Help')
    menu_español.add(tools_osint, version_pro, tools_extras, teams, help )
    bot.send_message(message.chat.id, 'Menu principal\nSeleciona una opción', reply_markup= menu_español)

#@bot.message_handler()  

bot.polling()