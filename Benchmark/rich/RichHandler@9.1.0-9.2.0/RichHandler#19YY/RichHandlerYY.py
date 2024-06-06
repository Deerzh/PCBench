import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(show_path=True, enable_link_path=True, markup=False, rich_tracebacks=True, tracebacks_width=80, highlighter=ReprHighlighter(), show_level=True, show_time=True)
