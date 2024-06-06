import logging
from rich.console import Console
from rich.logging import RichHandler
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.NOTSET, markup=False, highlighter=ReprHighlighter(), show_path=True, enable_link_path=True, console=Console())
