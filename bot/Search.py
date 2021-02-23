from typing import Union
from telegraph import Telegraph
import re

access_token = "e8200db69743a915f7c78c3791296f0ff0f77c4e5a3a47fd786073b42e7e"


class Search:

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


def get_count_pages() -> int:
    return Telegraph(access_token).get_page_list()["total_count"]


