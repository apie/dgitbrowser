#!/usr/bin/env python3
import sys
from pathlib import Path

from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import terminal
from pygments.util import ClassNotFound

import logging

logger = logging.getLogger(__name__)


def show_file(file_path: str):
    p = Path(file_path)
    if not p.exists():
        return logger.warning("File %s not found", p)

    try:
        lexer = get_lexer_for_filename(p)
    except ClassNotFound:
        logger.warning("No lexer found for file %s, showing without highlight:", p)
        return print(p.read_text())
    print(highlight(p.read_text(), lexer, terminal.TerminalFormatter()))


if __name__ == "__main__":
    file_path = sys.argv[1]
    show_file(file_path)
