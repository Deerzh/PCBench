import logging
from rich.console import Console
from rich.logging import RichHandler
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(level=logging.NOTSET, console=Console(), enable_link_path=True)
