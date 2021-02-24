from typing import Union
from telegraph import Telegraph
import re
import configparser
from bot.strings import Strings

config = configparser.ConfigParser()
config.read('bot/config.ini')
access_token = config.items("telegraph")[0][1]


class Search:
    """
    get all posts from telegraph account and filter them by query
    """

    def __init__(self, query: str = None):
        self.query = query

    def get_pages(self) -> dict:
        # get all our telegra.ph posts into a dict
        telegraph = Telegraph(access_token=access_token)
        return telegraph.get_page_list()

    def find(self) -> Union[list, None]:
        # filter posts by the query
        posts = []
        for post in self.get_pages()["pages"]:
            if re.findall(self.query, post["description"] + post["title"]):
                posts.append(post)
        return posts if posts else None


# get total number of posts
def get_count_pages() -> int:
    return Telegraph(access_token).get_page_list()["total_count"]
