import telebot

def chat_log(message):
    if message.from_user.first_name == 'None':
        first_name = '\b'
    if message.from_user.username == 'None':
        username = '\b'
    if message.from_user.last_name == 'None':
        last_name = '\b'

    chat_log = str('ID: ' + str(message.from_user.id) + '    Name: ' + str(message.from_user.first_name) + '   Username: ' + str(message.from_user.username) + '   Last Name: ' + str(message.from_user.last_name) + '     Says: ' + str(message.text) )
    return chat_log