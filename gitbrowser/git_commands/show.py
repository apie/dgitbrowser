#!/usr/bin/env python3
from datetime import datetime, timezone, timedelta


# Local
from gitbrowser.renderers.patch import highlight_patch

import logging

logger = logging.getLogger(__name__)


def show_stat(repo, commit):
    if commit.parents:
        rdiff = repo.diff(commit.parents[0], commit)
    else:
        rdiff = commit.tree.diff_to_tree(swap=True)
    print(f"{rdiff.stats.files_changed} files changed:")
    for d in rdiff.deltas:
        print(d.new_file.path)
    print()
    print(highlight_patch(rdiff.patch))


def git_show(repo, commit, with_stat=False):
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
    if with_stat:
        show_stat(repo, commit)
