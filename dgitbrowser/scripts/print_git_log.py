import click

# Local
from dgitbrowser.git_commands.log import git_log

import logging

logger = logging.getLogger(__name__)


@click.command()
@click.argument("path")
@click.option("--ncommits", default=3, help="Number of commits to show")
@click.option("--stat", default=False, is_flag=True)
def print_git_log(path, ncommits, stat):
    git_log(path, ncommits, stat)


if __name__ == "__main__":
    print_git_log()
