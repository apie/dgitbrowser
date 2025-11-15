import sys

import logging

# Local
from gitbrowser.renderers.file import highlight_file

logger = logging.getLogger(__name__)


def show_file(file_path: str):
    print(highlight_file(file_path))


if __name__ == "__main__":
    file_path = sys.argv[1]
    show_file(file_path)
