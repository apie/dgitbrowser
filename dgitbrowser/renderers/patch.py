from pygments import highlight
from pygments.lexers import diff
from pygments.formatters import terminal

import logging

logger = logging.getLogger(__name__)


def highlight_patch(patch: str):
    return highlight(patch, diff.DiffLexer(), terminal.TerminalFormatter())
