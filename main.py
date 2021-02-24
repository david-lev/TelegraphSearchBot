from pyrogram import Client
from bot.strings import Strings

if __name__ == '__main__':
    Client("bot/" + Strings.session_name, config_file="bot/config.ini").run()