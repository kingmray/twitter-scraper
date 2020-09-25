import csv
import locale
import logging
import sys
from typing import Optional

from .modules.profile import Profile
from .modules.trends import get_trends
from .modules.tweets import get_tweets

__all__ = ["Profile", "get_tweets", "get_trends"]


def write_tweets_to_csv(
        account: Optional[str] = None,
        page_limit: Optional = 1,
        filename: str = None,
    ):
    """Write posts from an account or group to a CSV file
     Args:
         account (str): Twitter account name e.g. "nike" or "nintendo"
         filename (str): Filename, defaults to <account or group>_posts.csv
         page_limit (Optional[int]): How many pages of posts to go through.
             Use None to try to get all of them.
     """
    # list_of_posts = get_tweets(query=account, pages=page_limit)
    list_of_posts = list(get_tweets(query=account, pages=page_limit))

    if not list_of_posts:
        print("Couldn't get any posts.", file=sys.stderr)
        return

    keys = list_of_posts[0].keys()

    if filename is None:
        filename = account + "_posts.csv"

    encoding = locale.getpreferredencoding()

    with open(filename, 'w', encoding=encoding) as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(list_of_posts)


def enable_logging(level=logging.INFO):
    handler = logging.StreamHandler()
    handler.setLevel(level)

    logger.addHandler(handler)
    logger.setLevel(level)

    # Disable logging by default


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
