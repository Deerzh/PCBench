from rich.columns import Columns
renderables = [f'Column {i}' for i in range(1, 4)]
columns = Columns(renderables=renderables, padding=(0, 1))
