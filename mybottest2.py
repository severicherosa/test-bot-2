import telebot
import re
#import logging
from telebot import types
#from func import chat_log
from log4python.Log4python import log
import sched
import time

scheduler = sched.scheduler(time.time, time.sleep) #aqui declare el scheduler

def print_event(name, start):
    now = time.time()
    elapsed = int(now - start)
    print('EVENT: {} elapsed={} name={}'.format(
        time.ctime(now), elapsed, name))


start = time.time()
print('START:', time.ctime(start))
scheduler.enter(2, 1, print_event, ('first', start))
scheduler.enter(62, 1, print_event, ('second', start))

scheduler.run()

TestLog = log("LogDemo")
TestLog.debug("Debug Log")
TestLog.info("Info Log")

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
TestLog.debug("Debug Log")
TestLog.info("Info Log")



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
    print(message.chat)
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
        opt1=types.KeyboardButton('Whois')
        opt2=types.KeyboardButton('Email check')
        opt3=types.KeyboardButton('Username')
        opt4=types.KeyboardButton('Enumeration')
        opt5=types.KeyboardButton('Metadata')
        opt6=types.KeyboardButton('Geo IP')
        opt7=types.KeyboardButton('Depixely')
        opt8=types.KeyboardButton('Main menu')
        menu_osint.add(opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8)
        bot.send_message(message.chat.id, 'Menu OSINT\nSelect an option',reply_markup=menu_osint)

        @bot.message_handler(regexp='Whois')
        def opt1(message):
            msg1 = bot.reply_to(message,'Enter website')
            bot.register_next_step_handler(msg1, process_whois)

        @bot.message_handler(regexp='Email check')
        def opt2(message):
            msg2 = bot.reply_to(message, 'Enter email')
            bot.register_next_step_handler(msg2, process_age_step)

        @bot.message_handler(regexp='Username')
        def opt3(message):
            bot.send_message(message.chat.id, 'Enter Username')

        @bot.message_handler(regexp='Enumeration')
        def opt4(message):
            bot.send_message(message.chat.id, 'Enter domain to evaluate')

        @bot.message_handler(regexp='Metadata')
        def opt5(message):
            bot.send_message(message.chat.id, 'Enter file')

        @bot.message_handler(regexp='Geo IP')
        def opt6(message):
            bot.send_message(message.chat.id, 'Enter IP')

        @bot.message_handler(regexp='Depixely')
        def opt7(message):
            bot.send_message(message.chat.id, 'Enter image JPEG / PNG')

        @bot.message_handler(regexp='Main menu')
        def opt8(message):
            bot.send_message(message.chat.id, 'Main menu\nselect an option', reply_markup=menu_english)

def process_whois(message):
    try:
        website = message.text
        #validate
        if is_valid_website(website):
            bot.send_message(message.chat.id,'valid website')
        else:
            bot.send_message(message.chat.id,'invalid website')
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_age_step(message):
    try:
        email = message.text
        if is_valid_email(email):
            bot.send_message(message.chat.id,'Valid email')
        else:
            bot.send_message(message.chat.id,'Invalid email')
    except Exception as e:
        bot.reply_to(message, 'oooops')



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
            
            
            #REGEX:

#regex de Dominio de sitio web
patron = re.compile("^((ht|f)tp(s?)\:\/\/|~/|/)?([\w]+:\w+@)?([a-zA-Z]{1}([\w\-]+\.)+([\w]{2,5}))(:[\d]{1,5})?((/?\w+/)+|/?)(\w+\.[\w]{3,4})?((\?\w+=\w+)?(&\w+=\w+)*)?")

def is_valid_website(website):
    if not isinstance(website, str):
        return False


    match_website = patron.match(website)

    if not match_website:
        try:
            website_encoded = website.encode('idna').decode('ascii')
        except UnicodeError:
            return False
        match_website = patron.match(website_encoded)

    return (match_website is not None)


#regex de email
body_regex = re.compile('''^(?!\.)([-a-z0-9!\#$%&'*+/=?^_`{|}~]|(?<!\.)\.)+(?<!\.)$''', re.VERBOSE | re.IGNORECASE)
domain_regex = re.compile('''(localhost|([a-z0-9]([-\w]*[a-z0-9])?\.)+[a-z]{2,})$''', re.VERBOSE | re.IGNORECASE)

def is_valid_email(email):
    if not isinstance(email, str) or not email or '@' not in email:
        return False
    
    body, domain = email.rsplit('@', 1)

    match_body = body_regex.match(body)
    match_domain = domain_regex.match(domain)

    if not match_domain:
        try:
            domain_encoded = domain.encode('idna').decode('ascii')
        except UnicodeError:
            return False
        match_domain = domain_regex.match(domain_encoded)

    return (match_body is not None) and (match_domain is not None)
 

bot.polling()