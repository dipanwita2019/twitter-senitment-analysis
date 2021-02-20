"""Console script for twitter_sentiment."""
import sys
import click

import twitter_sentiment.utils.logger as logger



@click.command()
def main(args=None):
    """Console script for twitter_sentiment."""
    click.echo("Replace this message by putting your code into "
               "twitter_sentiment.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    main_logger = logger.init_logger("twitter_sentiment.log", loglevel=logging.DEBUG)
    main_logger.info("Logging initialized")

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
