from rich.syntax import Syntax
syntax_obj = Syntax.from_path('/home/zhang/example.py',  'utf-8',  'monokai',  False,  True,  (1, 10), start_line=1, highlight_lines={2, 3}, code_width=50)
