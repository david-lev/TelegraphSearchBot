from pyrogram.types import *
from pyrogram import Client, filters
from bot.Search import Search, get_count_pages

share_url = "https://t.me/share/url?url="
channel = "https://t.me/joinchat/BpJrsvytyhIxYzBk"
image = "https://telegra.ph/file/09a0e9559c0961c379436.png"


def list_result(pages: list) -> list:
    results = []
    for page in pages:
        if page["title"].startswith("⛔"):
            continue

        results.append(InlineQueryResultArticle(
            title=page["title"] + " • " + page.get("author_name", ""),
            description=page["description"],
            thumb_url=page.get("image_url", image),

            input_message_content=InputTextMessageContent(
                message_text=f"[{page['title']}]({page['url']})\n\n{page.get('author_name', '')} • צפיות: {page['views']}",
                disable_web_page_preview=False),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("שיתוף הפוסט ♻️", url=share_url + page['url']),
                 InlineKeyboardButton("ערוץ אנדרוטיפס 📱", url=channel)]
            ])
        ))
    return results


@Client.on_inline_query()
def return_result(_, query: InlineQuery):

    match = Search(query.query).find()

    if match:
        query.answer(list_result(match),
                     switch_pm_text=f"from {len(match)} of {get_count_pages()} posts",
                     switch_pm_parameter="empty")
    elif not match:
        query.answer([], switch_pm_text="no results", switch_pm_parameter="no")

