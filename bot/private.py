from pyrogram import Client, filters
from pyrogram.types import *
from bot.inline import channel


@Client.on_message(filters.private & filters.command("start"))
def start_msg(_, message: Message):
    message.reply("start_msg", #TODO
                  reply_markup=InlineKeyboardMarkup([[
                      InlineKeyboardButton("ערוץ אנדרוטיפס 📱", url=channel),
                      InlineKeyboardButton("חפש מדריך 🔎", switch_inline_query_current_chat="")
                  ]]))
