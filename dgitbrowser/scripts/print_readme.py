import sys
from pathlib import Path

# Local
from dgitbrowser.renderers.file import highlight_file

import logging

logger = logging.getLogger(__name__)


def show_readme(repo_path: str):
    p = Path(repo_path)
    readme = p / "README.md"
    print("Readme:")
    if not readme.exists():
        return logger.warning("No README.md found")

    print(highlight_file(readme))


if __name__ == "__main__":
    repository_path = sys.argv[1]
    show_readme(repository_path)
