#!/usr/bin/env python3
import sys
from datetime import datetime, timezone, timedelta

import pygit2
from pygments import highlight
from pygments.lexers import diff
from pygments.formatters import terminal



def show_stat(commit):
    rdiff = repo.diff(commit.parents[0], commit)
    print(f"{rdiff.stats.files_changed} files changed:")
    for d in rdiff.deltas:
        print(d.new_file.path)
    print()
    print(highlight(rdiff.patch, diff.DiffLexer(), terminal.TerminalFormatter()))


def git_show(commit):
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
    show_stat(commit)


def git_log(repo, number_of_commits):
    last = repo[repo.head.target]
    for commit in repo.walk(last.id, pygit2.enums.SortMode.TIME):
        # print(commit.short_id, ':', commit.message.strip())
        git_show(commit)
        print()
        number_of_commits -= 1
        if number_of_commits <= 0:
            break


if __name__ == "__main__":
    repository_path = pygit2.discover_repository(sys.argv[1])
    repo = pygit2.Repository(repository_path)
    git_log(repo, 3)
