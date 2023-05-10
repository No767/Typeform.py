import re
from datetime import datetime
from typing import Union

from praw.models import Subreddit
from rich.table import Table


def formatSubredditTable(subreddit: Subreddit) -> Table:
    """Formats the given subreddit into a Rich Table

    Args:
        subreddit (Subreddit): Instance of praw.models.Subreddit

    Returns:
        Table: The formatted table
    """
    table = Table()
    table.add_column("Title")
    table.add_column("Flair")
    table.add_column("URL")
    table.add_column("Date Created")
    for posts in subreddit:
        table.add_row(
            posts.title,
            posts.author_flair_text or "None",
            posts.url,
            datetime.fromtimestamp(posts.created_utc).strftime("%a %d %b %Y %H:%M:%S"),
        )
    return table


# NOTE: This directly comes from Kumiko. This util function is still my own
# I am the owner and creator of Kumiko
# https://github.com/No767/Kumiko/blob/b9cce3efaafc79e1066bde6506523cab3ae9f6f0/Bot/Libs/utils/utils.py#LL48C1-L59C61
def parseSubreddit(subreddit: Union[str, None]) -> str:
    """Parses a subreddit name to be used in a reddit url

    Args:
        subreddit (Union[str, None]): Subreddit name to parse

    Returns:
        str: Parsed subreddit name
    """
    if subreddit is None:
        return "all"
    return re.sub(r"^[r/]{2}", "", subreddit, re.IGNORECASE)
