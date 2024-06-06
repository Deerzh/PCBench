import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(None, hidden_columns=None, conditional_formats=None, float_precision=3, column_formats=None, dtype_formats=None, sparklines=None, column_totals=None, has_header=True, hide_gridlines=False, row_heights=None, table_style=None, table_name=None, column_widths=None, position='A1', autofit=False, autofilter=True)
