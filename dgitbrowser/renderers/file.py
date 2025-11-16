#!/usr/bin/env python3
from pathlib import Path
from typing import Any

from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import terminal, html
from pygments.util import ClassNotFound

import logging

logger = logging.getLogger(__name__)


def highlight_file(file_path: str, use_html_formatter=False) -> Any:
    p = Path(file_path)
    if not p.exists():
        return logger.warning("File %s not found", p)

    try:
        lexer = get_lexer_for_filename(p)
    except ClassNotFound:
        logger.warning("No lexer found for file %s, showing without highlight:", p)
        return print(p.read_text())
    formatter = html.HtmlFormatter if use_html_formatter else terminal.TerminalFormatter
    return highlight(p.read_text(), lexer, formatter())


def highlight_file_html(file_path: str) -> Any:
    return highlight_file(file_path, use_html_formatter=True)
