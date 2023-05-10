import os
from datetime import datetime

import praw
import typer
from dotenv import load_dotenv
from praw.models import Submission
from rich.console import Console
from rich.markdown import Markdown
from typing_extensions import Annotated

from utils import formatSubredditTable, parseSubreddit

load_dotenv()

app = typer.Typer(
    help="Commands for browsing, and obtaining posts from subreddits",
    rich_markup_mode="rich",
)
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_ID"),
    client_secret=os.getenv("REDDIT_SECRET"),
    user_agent="testing folks",
)
console = Console()


@app.command()
def browse(
    subreddit: Annotated[str, typer.Option(help="The subreddit name to search")],
    filter: Annotated[str, typer.Option(help="filters")],
    amount: Annotated[int, typer.Option(help="The max amount of posts to show")] = 50,
) -> None:
    """
    Browse a subreddit, and returns a table of posts
    """
    currSub = reddit.subreddit(subreddit)
    subGen: Submission = (
        currSub.new(limit=amount)
        if filter == "new"
        else currSub.hot(limit=amount)
        if filter == "hot"
        else currSub.top(limit=amount)
    )
    console.print(formatSubredditTable(subGen))


@app.command()
def search(
    subreddit: Annotated[str, typer.Option(help="The subreddit name to search")],
    search: Annotated[str, typer.Option(help="The search term to look for")],
    amount: Annotated[int, typer.Option(help="The max amount of posts to show")] = 50,
) -> None:
    """
    Search for a search term within the given subreddit
    """
    currSub = reddit.subreddit(parseSubreddit(subreddit)).search(search, limit=amount)
    console.print(formatSubredditTable(currSub))


@app.command()
def random(
    subreddit: Annotated[str, typer.Option(help="The subreddit name to search")]
) -> None:
    """
    Gives you a random Reddit post
    """
    # sometimes it's just a ton of print statements
    currPost = reddit.subreddit(parseSubreddit(subreddit)).random()
    console.print(
        f"[bold][blue]{currPost.author.name}[/bold] - [bold][white]{currPost.title}[/bold]\n"
    )
    console.print(currPost.selftext, soft_wrap=True)
    console.print(f"\n({currPost.url})")
    console.print(Markdown("---"))
    console.print(f"Subreddit: r/{currPost.subreddit.display_name}")
    console.print(f"Upvotes: {currPost.score} ({currPost.upvote_ratio}%)")
    console.print(f"Number of Comments: {currPost.num_comments}")
    console.print(f"Flair: {currPost.link_flair_text}")
    console.print(f"Spoiler?: {currPost.spoiler}")
    console.print(f"NSFW?: {currPost.over_18}")
    console.print(
        f"Created At (UTC): {datetime.fromtimestamp(currPost.created_utc).strftime('%a %d %b %Y %H:%M:%S')}"
    )


@app.command()
def egg_irl(
    filter: Annotated[str, typer.Option(help="The filter to use")] = "new",
    amount: Annotated[int, typer.Option(help="The amount of posts to get")] = 50,
) -> None:
    """
    Returns a set amount of posts from r/egg_irl. Lol this is a joke.
    """
    currSub = reddit.subreddit("egg_irl")

    currFilter = currSub.comments.new(limit=amount)
    if filter in ["hot"]:
        currFilter = currSub.comments.hot(limit=amount)
    elif filter in ["top"]:
        currFilter = currSub.comments.top(limit=amount)

    console.print(formatSubredditTable(currSub))
