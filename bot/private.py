from bot.inline import *
from pyrogram import filters


# send start message
@Client.on_message(filters.command(["start", "start" + Strings.bot_username]))
def start_msg(_, message: Message):
    message.reply(Strings.start_message.format(f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"),
                  disable_web_page_preview=True,
                  reply_markup=InlineKeyboardMarkup([[
                      InlineKeyboardButton(Strings.channel_name, url=Strings.channel_url),
                      InlineKeyboardButton(Strings.search_button, switch_inline_query_current_chat="")
                  ]]))
