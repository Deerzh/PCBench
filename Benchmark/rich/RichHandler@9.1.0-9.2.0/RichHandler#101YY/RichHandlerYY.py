import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, console=Console(), show_level=True, show_time=True)
