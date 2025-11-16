import pygit2
import os.path

# Local
from dgitbrowser.git_commands.show import git_show

import logging

logger = logging.getLogger(__name__)


def git_log(path: str, number_of_commits: int, with_stat: bool = False):
    repository_git_path = pygit2.discover_repository(path)
    repo = pygit2.Repository(repository_git_path)
    last = repo[repo.head.target]
    for commit in repo.walk(last.id, pygit2.enums.SortMode.TIME):
        # print(commit.short_id, ':', commit.message.strip())
        if git_show(repo, commit, with_stat, path):
            number_of_commits -= 1
        if number_of_commits <= 0:
            break
