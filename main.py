#!/usr/bin/python3

# this bot made to search posts in telegra.ph account
# created by David Lev https://github.com/david-lev
# and Yehuda By https://github.com/M100achuz2

# https://github.com/david-lev/TelegraphSearchBot


from pyrogram import Client
from bot.strings import Strings

if __name__ == '__main__':
    Client("bot/" + Strings.bot_username[1:], config_file="bot/config.ini").run()
