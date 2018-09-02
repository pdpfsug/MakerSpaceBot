import os
import sys
import telepot
import time
from telepot.namedtuple import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from settings import TOKEN, start_msg, help_msg, info_msg, timeline_msg

# State for user
user_state = {}

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    chat_id = msg['chat']['id']
    command_input = msg['text']

    if command_input == "/start" or command_input == "/start@MakerSpaceFabrianoBot":
        bot.sendMessage(chat_id, start_msg)

    elif command_input == "/help" or command_input == "/help@MakerSpaceFabrianoBot":
        bot.sendMessage(chat_id, help_msg)

    elif command_input == "/info" or command_input == "/info@MakerSpaceFabrianoBot":
        bot.sendPhoto(chat_id, "https://i.imgur.com/reAMlzj.jpg")
        bot.sendMessage(chat_id, info_msg, parse_mode = "Markdown")

    elif command_input == "/timeline" or command_input == "/info@MakerSpaceFabrianoBot":
        markup = ReplyKeyboardMarkup(keyboard=[
                        ["1950"],
                        ["1966"],
                        ["1972"],
                        ["1988"],
                        ["1992"],
                        ["2000"],
                        ["2005"],
                        ["2006"],
                        ["2007"],
                        ["2015"],
                        ["2016"],
                        ["2017"]])

        bot.sendMessage(chat_id, timeline_msg, reply_markup=markup)

        # Set the new user_state
        user_state[chat_id] = 1

    elif user_state[chat_id] == 1:

        if command_input == "1950":
            bot.sendMessage(chat_id, "1950 STYLE", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))
        elif command_input == "1966":
            bot.sendMessage(chat_id, "1966 STYLE", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))
        elif command_input == "1972":
            bot.sendMessage(chat_id, "1972 STYLE", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))
        elif command_input == "1988":
            bot.sendMessage(chat_id, "1988 STYLE", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))
        elif command_input == "1992":
            bot.sendMessage(chat_id, "1992 STYLE", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))
        elif command_input == "2000":
            bot.sendMessage(chat_id, "2000 STYLE", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))
        elif command_input == "2005":
            bot.sendMessage(chat_id, "2005 STYLE", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))
        elif command_input == "2006":
            bot.sendMessage(chat_id, "2006 STYLE", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))
        elif command_input == "2007":
            bot.sendMessage(chat_id, "2007 STYLE", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))
        elif command_input == "2015":
            bot.sendMessage(chat_id, "2015 STYLE", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))
        elif command_input == "2016":
            bot.sendMessage(chat_id, "2016 STYLE", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))
        elif command_input == "2017":
            bot.sendMessage(chat_id, "2017 STYLE", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))

        ####################################################
        #    Inserire le tappe per la visualizzazione      #
        #    delle informazioni relative all'Evoluzione    #
        #    dei Chat Bot, link -> https://goo.gl/FXVbNu   #
        ####################################################

        else:
            bot.sendMessage(chat_id, "Il messaggio inserito non è valido", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))

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

    bot.message_loop({'chat': handle})

finally:
    # Remove PID file on exit
    os.unlink(pidfile)

while 1:
    time.sleep(10)
