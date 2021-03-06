import configparser


class Strings:
    config = configparser.ConfigParser()
    config.read('bot/config.ini')
    bot_username = config.items("telegram")[0][1]
    # bot strings
    channel_name = "To our channel"  # button to your channel
    channel_url = "https://t.me/joinchat/BpJrsvytyhIxYzBk"  # link to your channel (for credit)
    search_button = "Search article 🔎"  # search articles button
    default_image = "https://telegra.ph/images/logo.png"  # url to image when there is no image in article preview
    char_ignore = "⛔"  # Ignore posts whose title starts with the defined emoji ("⛔ Title")
    share_post = "Share this post ♻️"  # share post button
    count_posts = "Showing {} results out of {} posts"  # count of results in search window
    no_results = "No results • try again"  # when there is no results

# start message in private and groups
    start_message = """Hi, {}!

**Welcome to the search bot from [Androtips!]({})**

This bot will help you search articles and tutorials on our channel.
 In each chat, type the bot user followed by the search words:
`{} a word`
Choose the article you want and get the article in a Instant View!

This bot made with ❤️ by [Androtips Team](https://t.me/joinchat/BpJrsvytyhIxYzBk).
"""
