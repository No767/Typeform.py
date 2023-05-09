import typer
import praw

app = typer.Typer(rich_markup_mode="rich")

@app.command()
def search(subreddit: str):
    reddit = praw.Reddit()
    currSub = reddit.subreddit(subreddit)
    print(currSub.title)
    
if __name__ == "__main__":
    app()