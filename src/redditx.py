# import yaml
import praw
from charset_normalizer import md
# See https://stackoverflow.com/a/74540217

# config = {}

# with open(Path(__file__).parent.joinpath("config.yaml"), "r") as f:
#    config = yaml.safe_load(f)

reddit = praw.Reddit(user_agent="testing folks")
