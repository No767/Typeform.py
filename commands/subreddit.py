import typer
import praw
from dotenv import load_dotenv
import os
from typing_extensions import Annotated
from rich.console import Console
from praw.models import Submission
from commands.utils import formatSubredditTable
load_dotenv()

app = typer.Typer(rich_markup_mode="rich")
reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_ID"),
        client_secret=os.getenv("REDDIT_SECRET"),
        user_agent="testing folks"
    )
console = Console()

@app.command()
def browse(subreddit: str, filter: Annotated[str, typer.Option(help="filters")]):
    currSub = reddit.subreddit(subreddit)
    subGen: Submission = currSub.new(limit=15) if filter == "new" else currSub.hot(limit=15) if filter == "hot" else currSub.top(limit=15)
    console.print(formatSubredditTable(subGen))

@app.command()
def search(subreddit: str, search: str):
    currSub = reddit.subreddit(subreddit).search(search)
    console.print(formatSubredditTable(currSub))

@app.command()
def random(subreddit: str):
    currSub = reddit.subreddit(subreddit).random()
    console.print(formatSubredditTable(currSub))