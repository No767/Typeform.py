from datetime import datetime

import typer
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
from rich.tree import Tree
from typing_extensions import Annotated

from redditx import reddit
from utils import parseRedditor

load_dotenv()

app = typer.Typer(
    help="Commands for searching and obtaining Redditors (users)",
    rich_markup_mode="rich",
)

console = Console()


@app.command()
def search(
    redditor: Annotated[str, typer.Option(help="The name of the redditor to search")]
) -> None:
    """
    Provides info about the given Redditor
    """
    currUser = reddit.redditor(parseRedditor(redditor))
    console.print(f"[bold][blue]{currUser.name}[/bold] - {currUser.icon_img}\n")
    console.print(f"Karma (total): {currUser.link_karma + currUser.comment_karma}")
    console.print(
        f"Created at (UTC): {datetime.fromtimestamp(currUser.created_utc).strftime('%a %d %b %Y %H:%M:%S')}"
    )
    console.print(f"Is Mod?: {currUser.is_mod}")
    console.print(Markdown("---"))
    currTree = Tree(f"[bold][blue]{currUser.name}'s Comments (newest)[/bold]")
    for posts in currUser.comments.new():
        currSub = currTree.add(
            f"[bold][white]r/{posts.subreddit.display_name}[/bold] ({posts.score} Upvotes)"
        )
        currSub.add(Markdown(posts.body))
        currSub.add(f"[blue]https://reddit.com{posts.permalink}[/blue]")
    console.print(currTree)
