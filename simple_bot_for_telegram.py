import telebot
import logging
from telebot import types


#logger = telebot.logger
#telebot.logger.setLevel(logging.DEBUG)
TOKEN = '1945274113:AAEYimj6dtgvk6QfNyNu8XzIhbn3dLY7koo'
CHAT_ID = ''
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def menu(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_comment = types.InlineKeyboardButton(text='Evaluar el servicio de coworking', callback_data='сomment')
    item_help = types.InlineKeyboardButton(text='Sala de chat 👌', callback_data='help')
    item_price = types.InlineKeyboardButton(text='Precio de los servicios', callback_data='url')
    item_info = types.InlineKeyboardButton(text='Instagram', url='https://instagram.com/coworkingifgzp?utm_medium=copy_link')
    markup_inline.add(item_comment,item_help,item_price, item_info )
    bot.send_message(message.chat.id, '¡Hola, bienvenido a IFGCoworking! Haz tu elección',
                     reply_markup=markup_inline
                     )
    



@bot.callback_query_handler(func= lambda call: True)
def answer(call):
    if call.data == 'сomment':
        comment(call.message)
    elif call.data == 'help':
        help(call.message)
    elif call.data == 'url':
        url(call.message)
    elif call.data == 'start':
        menu(call.message)
    elif call.data == 'info':
        info(call.message)
    elif call.data == 'btnCoworkingCALL':
            btnCoworkingCALL(call.message)
    elif call.data == 'btn_text_review_call':
            btn_text_review_call(call.message)
    elif call.data == 'Star1c':
        Star1c(call.message)
    elif call.data == 'Star2c':
        Star2c(call.message)
    elif call.data == 'Star3c':
        Star3c(call.message)
    elif call.data == 'Star4c':
        Star4c(call.message)
    elif call.data == 'Star5c':
        Star5c(call.message)

@bot.message_handler(commands= ['info'])
def info(message):
    markup = types.InlineKeyboardMarkup()
    insta = types.InlineKeyboardButton(text='Instagram', url='https://instagram.com/coworkingifgzp?utm_medium=copy_link')
    markup.add(insta)
   


@bot.message_handler(commands = ['url'])
def url(message):
    text_for_items = 'Internet alta velocidad, aire acondicionado, área de juegos, estacionamiento, uso de equipo técnico (mfu), té, café y galletas'
    bot.send_photo(message.chat.id, 'http://www.ifg-ua.com/wp-content/uploads/2021/03/IMG_7545-scaled-e1616861838291.jpg')
    bot.send_message(message.chat.id, ' ₴ 50 por ahora')
    bot.send_message(message.chat.id, text_for_items)
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='LUGAR DE TRABAJO', url='http://www.ifg-ua.com/arenda-2/')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Orden.", reply_markup = markup)

    bot.send_photo(message.chat.id, 'http://www.ifg-ua.com/wp-content/uploads/2021/03/IMG_7537-scaled.jpg')
    bot.send_message(message.chat.id, '  ₴ 1800 por ahora  ')
    bot.send_message(message.chat.id, text_for_items)
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='LUGAR SIN FIJAR', url='http://www.ifg-ua.com/arenda-2/')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Orden", reply_markup = markup)

    bot.send_photo(message.chat.id, 'http://www.ifg-ua.com/wp-content/uploads/2021/03/IMG_7541-scaled-e1616856579779.jpg')
    bot.send_message(message.chat.id, '  ₴ 2250 por ahora ')
    bot.send_message(message.chat.id, text_for_items)
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='ФІКСОВАНЕ МІСЦЕ', url='http://www.ifg-ua.com/arenda-2/')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Orden", reply_markup = markup)

    bot.send_photo(message.chat.id, 'http://www.ifg-ua.com/wp-content/uploads/2021/03/IMG_7546-scaled.jpg')
    bot.send_message(message.chat.id, '  ₴ 200 por ahora ')
    bot.send_message(message.chat.id, text_for_items)
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='UNIVERSAL HALL 30 ОСІБ ', url='http://www.ifg-ua.com/arenda-2/')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Orden", reply_markup = markup)

    bot.send_photo(message.chat.id, 'http://www.ifg-ua.com/wp-content/uploads/2021/03/IMG_7544-scaled-e1616856615817.jpg')
    bot.send_message(message.chat.id, ' ₴ 150 por ahora ')
    bot.send_message(message.chat.id, text_for_items)
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='ПЕРЕГОВОРНА 5 - 6 ОСІБ ', url='http://www.ifg-ua.com/arenda-2/')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Orden", reply_markup = markup)

    bot.send_photo(message.chat.id, 'http://www.ifg-ua.com/wp-content/uploads/2021/03/IMG_7536-scaled.jpg')
    bot.send_message(message.chat.id, '  ₴ 275 por ahora ')
    bot.send_message(message.chat.id, text_for_items)
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='BUSINESS CLASS 70 ОСІБ', url='http://www.ifg-ua.com/arenda-2/')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Orden", reply_markup = markup)
    menu(message)


@bot.message_handler(commands=['help']) 
def help(message):
    msg = bot.send_message(message.chat.id, 'Доброго дня! Чим я можу Вам допомогти?')
    bot.register_next_step_handler(msg, help_request)


def help_request(message):
    bot.send_message(message.chat.id, 'Ваше питання переданий адміністратору, найближчим часов з Вами зв`яжуться')
    Nickname = '@' + message.from_user.username
    bot.send_message('use logger to know id of chat, what you need to sent stars', '{0}\n{1}\n{2}\n{3}\n{4}'.format(message.text,
                                                                      message.chat.id,
                                                                      message.from_user.first_name,
                                                                      message.from_user.last_name,
                                                                      Nickname))





@bot.message_handler(commands=['comment']) 
def comment(review):
    markup = types.InlineKeyboardMarkup()
    coworking_button = types.InlineKeyboardButton(text='Зірочки', callback_data='btnCoworkingCALL')
    btn_text_review_call = types.InlineKeyboardButton(text='Залиште відгук', callback_data='btn_text_review_call')
    markup.add(coworking_button,btn_text_review_call)
    adm = bot.send_message(review.chat.id, 'Оцініть сервіс коворкінга, нам важлива Ваша думка', reply_markup = markup)
    bot.register_next_step_handler(adm, btn_text_review_call, btnCoworkingCALL, Star1c,Star2c,Star3c,Star4c,Star5c)








@bot.message_handler(commands=['btnCoworkingCALL'])
def btnCoworkingCALL(review):
    markupCow = types.InlineKeyboardMarkup()
    btnStar1c = types.InlineKeyboardButton(text='⭐️', callback_data='Star1c')
    btnStar2c = types.InlineKeyboardButton(text='⭐️⭐️', callback_data='Star2c')
    btnStar3c = types.InlineKeyboardButton(text='⭐️⭐️⭐️', callback_data='Star3c')
    btnStar4c = types.InlineKeyboardButton(text='⭐️⭐️⭐️⭐️', callback_data='Star4c')
    btnStar5c = types.InlineKeyboardButton(text='⭐️⭐️⭐️⭐️⭐️', callback_data='Star5c')
    markupCow.add(btnStar1c,btnStar2c,btnStar3c,btnStar4c,btnStar5c)
    bot.send_message(review.chat.id, 'Зробіть Ваш вибір',
                     reply_markup=markupCow
                     )

def coworking_request(review):
    bot.send_message(review.chat.id, 'Дякуємо за Ваш відгук.')
    Nickname = '@' + review.from_user.username
    





@bot.message_handler(commands=['btn_text_review_call'])
def btn_text_review_call(review):
    msg = bot.send_message(review.chat.id, 'Введіть Ваш відгук')
    bot.register_next_step_handler(msg, text_request)

def text_request(review):
    bot.send_message(review.chat.id, 'Дякуємо за Ваш відгук.')
    Nickname = '@' + review.from_user.username
    bot.send_message('use logger to know id of chat, what you need to sent stars', '{0}\n{1}\n{2}\n{3}\n{4}'.format(review.text,
                                                                      review.chat.id,
                                                                      review.from_user.first_name,
                                                                      review.from_user.last_name,
                                                                      Nickname))




@bot.message_handler(commands=['Star1c']) 
def Star1c(review):
    bot.send_message('use logger to know id of chat, what you need to sent stars', '⭐️')
    bot.send_message(review.chat.id, 'Дякуємо за Ваш вибір1')
    
@bot.message_handler(commands=['Star2c']) 
def Star2c(review):
    bot.send_message('use logger to know id of chat, what you need to sent stars', '⭐️⭐️')
    bot.send_message(review.chat.id, 'Дякуємо за Ваш вибір!')

@bot.message_handler(commands=['Star3c']) 
def Star3c(review):
    bot.send_message('use logger to know id of chat, what you need to sent stars', '⭐️⭐️⭐️')
    bot.send_message(review.chat.id, 'Дякуємо за Ваш вибір!')

@bot.message_handler(commands=['Star4c']) 
def Star4c(review):
    bot.send_message('use logger to know id of chat, what you need to sent stars', '⭐️⭐️⭐️⭐️')
    bot.send_message(review.chat.id, 'Дякуємо за Ваш вибір!')

@bot.message_handler(commands=['Star5c']) 
def Star5c(review):
    bot.send_message('use logger to know id of chat, what you need to sent stars', '⭐️⭐️⭐️⭐️⭐️')
    bot.send_message(review.chat.id, 'Дякуємо за Ваш вибір!')





bot.polling(none_stop=True, interval=0)
