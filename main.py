import typer
import praw
from dotenv import load_dotenv
import os
from typing import Literal
from typing_extensions import Annotated
from rich.columns import Columns
from rich import print
from rich.table import Table
from rich.console import Console
load_dotenv()

app = typer.Typer(rich_markup_mode="rich")
console = Console()

@app.command()
def main():
    print("help")
@app.command()
def subreddit(subreddit: str, filter: Annotated[str, typer.Option(help="filters")]):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_ID"),
        client_secret=os.getenv("REDDIT_SECRET"),
        user_agent="testing folks"
    )
    currSub = reddit.subreddit(subreddit)
    subGen = currSub.new(limit=15) if filter == "new" else currSub.hot(limit=15) if filter == "hot" else currSub.top(limit=15)
    table = Table()
    table.add_column("Title")
    table.add_column("URL")
    for posts in subGen: table.add_row(posts.title, posts.url)
    console.print(table)
    

if __name__ == "__main__":
    app()