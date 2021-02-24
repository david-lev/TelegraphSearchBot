from pyrogram.types import *
from pyrogram import Client
from bot.Search import *

# url variables
share_url = "https://t.me/share/url?url="


# exclude posts
def list_result(pages: list) -> list:
    results = []
    for page in pages:
        if page["title"].startswith(Strings.char_ignore):
            continue

        results.append(InlineQueryResultArticle(
            title=page["title"] + " • " + page.get("author_name", ""),
            description=page["description"],
            thumb_url=page.get("image_url", Strings.default_image),

            input_message_content=InputTextMessageContent(
                message_text=f"[{page['title']}]({page['url']})\n\n"
                             f"{page.get('author_name', '')} • {Strings.views}: {page['views']}",
                disable_web_page_preview=False),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(Strings.share_post, url=share_url + page['url']),
                 InlineKeyboardButton(Strings.channel_name, url=Strings.channel_url)]
            ])
        ))
    return results


@Client.on_inline_query()
def return_result(_, query: InlineQuery):
    match = Search(query.query).find()

    if match:
        query.answer(list_result(match),
                     switch_pm_text=Strings.count_posts.format(len(match), get_count_pages()),
                     switch_pm_parameter="empty")
    elif not match:
        query.answer([], switch_pm_text=Strings.no_results, switch_pm_parameter="no")
