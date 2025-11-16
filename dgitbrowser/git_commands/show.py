#!/usr/bin/env python3
from datetime import datetime, timezone, timedelta
from functools import lru_cache
import os.path


# Local
from dgitbrowser.renderers.patch import highlight_patch

import logging

logger = logging.getLogger(__name__)


@lru_cache
def get_rdiff(repo, commit):
    if commit.parents:
        return repo.diff(commit.parents[0], commit)
    return commit.tree.diff_to_tree(swap=True)


def show_stat(repo, commit):
    rdiff = get_rdiff(repo, commit)
    print(f"{rdiff.stats.files_changed} files changed:")
    for d in rdiff.deltas:
        print(d.new_file.path)
    print()
    # print(highlight_patch(rdiff.patch))


def git_show(repo, commit, with_stat=False, path: str = ""):
    path = os.path.abspath(path)
    if path == os.path.abspath(repo.path + ".."):
        # Requested path is the repo path, so do not pass it.
        path = ""
    # If specific path provided, dont show commits without that path.
    if path and path not in [d.new_file.path for d in get_rdiff(repo, commit).deltas]:
        print('aha het zijn relatieve paths uiteraard, dus moet ze nog relatief aan elkaar maken')
        # FIXME
        return
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
    print()
