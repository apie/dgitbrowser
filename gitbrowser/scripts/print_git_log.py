import click

# Local
from gitbrowser.git_commands.log import git_log

import logging

logger = logging.getLogger(__name__)


@click.command()
@click.argument("repository_path")
@click.option("--ncommits", default=3, help="Number of commits to show")
@click.option("--stat", default=False, is_flag=True)
def print_git_log(repository_path, ncommits, stat):
    git_log(repository_path, ncommits, stat)


if __name__ == "__main__":
    print_git_log()
