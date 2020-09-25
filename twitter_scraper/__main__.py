import argparse
import logging

from twitter_scraper import write_tweets_to_csv, enable_logging


def run():
    """twitter-scraper entry point when used as a script"""
    parser = argparse.ArgumentParser(
        prog='twitter-scraper', description="Scrape twitter public pages without an API key",
    )
    parser.add_argument('account', type=str, help="twitter account")
    parser.add_argument('-f', '--filename', type=str, help="Output filename")
    parser.add_argument('-p', '--pages', type=int, help="Number of pages to download", default=10)
    parser.add_argument('-v', '--verbose', action='count', help="Enable logging", default=0)
    args = parser.parse_args()

    # Enable logging
    if args.verbose > 0:
        args.verbose = min(args.verbose, 3)
        level = {1: logging.WARNING, 2: logging.INFO, 3: logging.DEBUG}[args.verbose]
        enable_logging(level)

    write_tweets_to_csv(account=args.account, filename=args.filename, page_limit=args.pages)


if __name__ == '__main__':
   run()

