#!/usr/bin/env python3
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

import pygit2
from pygments import highlight
from pygments.lexers import diff, markup
from pygments.formatters import terminal

import logging

logger = logging.getLogger(__name__)


def show_readme(repo_path: str):
    p = Path(repo_path)
    readme = p / "README.md"
    print("Readme:")
    if not readme.exists():
        return logger.warning("No README.md found")

    print(
        highlight(
            readme.read_text(), markup.MarkdownLexer(), terminal.TerminalFormatter()
        )
    )


def show_stat(repo, commit):
    if commit.parents:
        rdiff = repo.diff(commit.parents[0], commit)
    else:
        rdiff = commit.tree.diff_to_tree(swap=True)
    print(f"{rdiff.stats.files_changed} files changed:")
    for d in rdiff.deltas:
        print(d.new_file.path)
    print()
    print(highlight(rdiff.patch, diff.DiffLexer(), terminal.TerminalFormatter()))


def git_show(repo, commit):
    tzinfo = timezone(timedelta(minutes=commit.author.offset))

    dt = datetime.fromtimestamp(float(commit.author.time), tzinfo)

    timestr = dt.strftime("%c %z")

    msg = "\n".join(
        [
            f"commit {commit.id}",
            f"Author: {commit.author.name} <{commit.author.email}>",
            f"Date:   {timestr}",
            "",
            commit.message,
        ]
    )
    print(msg)
    show_stat(repo, commit)


def git_log(repo, number_of_commits):
    last = repo[repo.head.target]
    for commit in repo.walk(last.id, pygit2.enums.SortMode.TIME):
        # print(commit.short_id, ':', commit.message.strip())
        git_show(repo, commit)
        print()
        number_of_commits -= 1
        if number_of_commits <= 0:
            break


if __name__ == "__main__":
    repository_path = sys.argv[1]
    repository_git_path = pygit2.discover_repository(repository_path)
    repo = pygit2.Repository(repository_git_path)
    git_log(repo, 3)
    show_readme(repository_path)
