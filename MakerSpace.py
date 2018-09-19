import os
import sys
import telepot
import time
from telepot.namedtuple import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from settings import TOKEN, start_msg, help_msg, info_msg, timeline_msg, msg_style

# State for user
user_state = {}

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    chat_id = msg['chat']['id']
    command_input = msg['text']

    # Getting information to print debug msg
    try:
        username  = msg['from']['username']
    except:
        username  = "Not defined"

    try:
        full_name = msg['from']['first_name'] + ' ' + msg['from']['last_name']
    except:
        full_name = "Not defined"

    if username == "Not defined":
        username = full_name

    # Prints msg from the user
    print("Msg from @{}[{}]: \"{}\"".format(username.ljust(16), chat_id, command_input))

    # Commands
    if command_input == "/start" or command_input == "/start@MakerSpaceFabrianoBot":
        bot.sendMessage(chat_id, start_msg)

    elif command_input == "/help" or command_input == "/help@MakerSpaceFabrianoBot":
        bot.sendMessage(chat_id, help_msg)

    elif command_input == "/info" or command_input == "/info@MakerSpaceFabrianoBot":
        bot.sendPhoto(chat_id, "https://i.imgur.com/reAMlzj.jpg")
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [dict(text = 'Pagina successiva  >>', callback_data = 'info_next_page_1')]])

        bot.sendMessage(chat_id, info_msg[0], reply_markup=keyboard, parse_mode = "Markdown")

    elif command_input == "/timeline" or command_input == "/timeline@MakerSpaceFabrianoBot" or command_input == "Indietro":
        markup = ReplyKeyboardMarkup(keyboard=[
                        ["1950"],
                        ["1966"],
                        ["1972"],
                        ["1988"],
                        ["1992 - Parte 1"],
                        ["1992 - Parte 2"],
                        ["2000"],
                        ["2005"],
                        ["2006"],
                        ["2007"],
                        ["2015"],
                        ["2016 - Parte 1"],
                        ["2016 - Parte 2"],
                        ["2016 - Parte 3"],
                        ["2017 - Parte 1"],
                        ["2017 - Parte 2"]])

        bot.sendMessage(chat_id, timeline_msg, reply_markup=markup)

        # Set the new user_state
        user_state[chat_id] = 1

    elif user_state[chat_id] == 1:
        try:
            markup = ReplyKeyboardMarkup(keyboard=[["Indietro"]], resize_keyboard=True)
            bot.sendMessage(chat_id, msg_style[command_input], reply_markup=markup)
        except KeyError:
            bot.sendMessage(chat_id, "La data inserita non è valida", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))

        ####################################################
        #    Inserire le tappe per la visualizzazione      #
        #    delle informazioni relative all'Evoluzione    #
        #    dei Chat Bot, link -> https://goo.gl/FXVbNu   #
        ####################################################

    else:
        bot.sendMessage(chat_id, "Il messaggio inserito non è valido", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))

def on_callback_query(msg):
    """
    Function to manage callback query from callback buttons in inline keyboards
    """
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    if query_data == 'info_next_page_0':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [dict(text = 'Pagina successiva  >>', callback_data = 'info_next_page_1')]])

        bot.editMessageText((from_id, msg['message']['message_id']), info_msg[0], reply_markup = keyboard, parse_mode = "Markdown")
        bot.answerCallbackQuery(query_id, text = "Buona lettura!")

    if query_data == 'info_next_page_1':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [dict(text = '<<  Pagina precendente', callback_data = 'info_next_page_0'), dict(text = 'Pagina successiva  >>', callback_data = 'info_next_page_2')]])

        bot.editMessageText((from_id, msg['message']['message_id']), info_msg[1], reply_markup = keyboard, parse_mode = "Markdown")
        bot.answerCallbackQuery(query_id, text = "Buona lettura!")

    if query_data == 'info_next_page_2':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [dict(text = '<<  Pagina precendente', callback_data = 'info_next_page_1')]])

        bot.editMessageText((from_id, msg['message']['message_id']), info_msg[2], reply_markup = keyboard, parse_mode = "Markdown")
        bot.answerCallbackQuery(query_id, text = "Buona lettura!")

# PID file
pid = str(os.getpid())
pidfile = "/tmp/mkbot.pid"

# Check if PID exist
if os.path.isfile(pidfile):
    print("%s already exists, exiting!" % pidfile)
    sys.exit()

# Create PID file
f = open(pidfile, 'w')
f.write(pid)
f.close()

print('Vediamo quello che succede...')

try:
    bot = telepot.Bot(TOKEN)

    bot.message_loop({'chat': handle,
                      'callback_query': on_callback_query})

finally:
    # Remove PID file on exit
    os.unlink(pidfile)

while 1:
    time.sleep(10)
