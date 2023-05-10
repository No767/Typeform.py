from rich.table import Table
from datetime import datetime
from praw.models import Subreddit

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
        table.add_row(posts.title, posts.author_flair_text or "None", posts.url, datetime.fromtimestamp(posts.created_utc).strftime("%a %d %b %Y %H:%M:%S"))
    return table