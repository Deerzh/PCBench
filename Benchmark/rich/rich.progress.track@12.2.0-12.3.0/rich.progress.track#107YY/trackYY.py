from rich.progress import track
from rich.console import Console
console = Console()
sequence = range(100)
track(sequence,  'Working...',  None,  True,  console,  False,  None,  10,  'bar.back',  'bar.complete',  'bar.finished',  'bar.pulse', update_period=0.1, disable=False)
