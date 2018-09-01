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
        bot.sendMessage(chat_id, timeline_msg)

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