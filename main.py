import typer
import praw
from dotenv import load_dotenv
from datetime import datetime
import os
from typing import Literal
from typing_extensions import Annotated
from rich.columns import Columns
from rich import print
from rich.table import Table
from rich.console import Console
load_dotenv()
import commands.subreddit as commandSubreddit
app = typer.Typer(rich_markup_mode="rich")
console = Console()

@app.command()
def main():
    pass

app.add_typer(commandSubreddit.app, name="subreddit")

if __name__ == "__main__":
    app()