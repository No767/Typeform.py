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
    table = Table(expand=True)
    table.add_column("Title")
    table.add_column("Author")
    table.add_column("User Flair")
    table.add_column("Upvotes (w/ Ratio)")
    table.add_column("NSFW?")
    table.add_column("# of Comments")
    table.add_column("URL")
    table.add_column("Date Created")
    for posts in subreddit:
        table.add_row(
            posts.title,
            posts.author.name,
            posts.author_flair_text or "None",
            f"{posts.score} ({posts.upvote_ratio}%)",
            f"{posts.over_18}",
            f"{posts.num_comments}",
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


# U know i might use this in Kumiko...
# Someone remind me to port this over
def parseRedditor(redditor: Union[str, None]) -> str:
    """Parses a Redditor's name to be used in PRAW's redditor lookup

    Args:
        redditor (Union[str, None]): Redditor name to parse

    Returns:
        str: Parsed subreddit name
    """
    if redditor is None:
        return "all"
    return re.sub(r"^[u/]{2}", "", redditor, re.IGNORECASE)
