import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(None,  None, position='A1', column_widths=None, autofilter=True, column_totals=None, sparklines=None, conditional_formats=None, dtype_formats=None, has_header=True, row_heights=None, table_name=None, table_style=None, column_formats=None, float_precision=3)
