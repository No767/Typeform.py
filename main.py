import typer
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()
import commands.comments as commandComments
import commands.redditor as commandRedditor
import commands.subreddit as commandSubreddit

app = typer.Typer(rich_markup_mode="rich")
console = Console()


@app.command()
def main():
    pass


app.add_typer(commandSubreddit.app, name="subreddit")
app.add_typer(commandRedditor.app, name="redditor")
app.add_typer(commandComments.app, name="comments")

if __name__ == "__main__":
    app()
