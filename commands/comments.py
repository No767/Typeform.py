import os
from datetime import datetime

import praw
import typer
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
from rich.tree import Tree
from typing_extensions import Annotated

from utils import parseRedditor

load_dotenv()

app = typer.Typer(rich_markup_mode="rich")
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_ID"),
    client_secret=os.getenv("REDDIT_SECRET"),
    user_agent="testing folks",
)
console = Console()


@app.command()
def redditor(
    redditor: Annotated[str, typer.Option(help="The name of the redditor to search")],
    filter: Annotated[str, typer.Option(help="The filter to use")] = "new",
) -> None:
    # Jerry said not to code golf so...

    currUser = reddit.redditor(parseRedditor(redditor))

    currFilter = currUser.comments.new()
    if filter in ["hot"]:
        currFilter = currUser.comments.hot()
    elif filter in ["top"]:
        currFilter = currUser.comments.top()

    currTree = Tree(f"[bold][blue]{currUser.name}'s Comments[/bold]")
    for posts in currFilter:
        currSub = currTree.add(
            f"[bold][white]r/{posts.subreddit.display_name}[/bold] ({posts.score} Upvotes)"
        )
        currSub.add(Markdown(posts.body))
        currSub.add(f"[blue]https://reddit.com{posts.permalink}[/blue]")

    console.print(currTree)


# Later on this will not use an ID based system.
# Instead a dropdown menu will show up, and you can choose the post from there instead
# TESTING URL: https://www.reddit.com/r/egg_irl/comments/136xye0/eggirl/
# also could be handled in parallel w/ multithreading for increased performance
@app.command()
def posts(
    id: Annotated[
        str, typer.Option(help="The post ID. Later on this will not need this")
    ],
    filter: Annotated[str, typer.Option(help="The filter to use")] = "new",
) -> None:
    currPost = reddit.submission(id=id)

    currFilter = "new"
    if filter in ["hot"]:
        currFilter = "hot"
    elif filter in ["top"]:
        currFilter = "top"

    currPost.comment_sort = currFilter

    currTree = Tree(f"[bold][blue]{currPost.title}[/bold] - {currPost.author.name}")
    resTree = currTree.add(Markdown(currPost.selftext))
    resTree.add(f"[blue]https://reddit.com{currPost.permalink}[/blue]")
    currPost.comments.replace_more()
    for comments in currPost.comments:
        currAuthor = comments.author
        currAuthorName = comments.author.name if currAuthor is not None else "[deleted]"
        subTree = currTree.add(
            f"[bold][bright_blue]{currAuthorName}[/bright_blue][/bold] ({comments.score} Upvotes) - ({datetime.fromtimestamp(comments.created_utc).strftime('%Y-%m-%d %H:%M:%S')})",
            guide_style="bright_blue",
        )
        subTree.add(Markdown(comments.body))
        if len(comments.replies) > 0:
            for replies in comments.replies:
                currReplyName = "[deleted]"
                if replies.author is not None:
                    currReplyName = replies.author.name
                subTree2 = subTree.add(
                    f"[bold][orchid]{currReplyName}[/orchid][/bold] ({replies.score} Upvotes) - ({datetime.fromtimestamp(replies.created_utc).strftime('%Y-%m-%d %H:%M:%S')})",
                    guide_style="orchid",
                )
                subTree2.add(Markdown(replies.body))

    console.print(currTree)
