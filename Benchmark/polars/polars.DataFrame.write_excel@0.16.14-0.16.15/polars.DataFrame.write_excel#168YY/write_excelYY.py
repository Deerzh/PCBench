import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(None, dtype_formats=None, table_style=None, has_header=True, table_name=None, autofit=False, row_heights=None, worksheet=None, hidden_columns=None, column_widths=None, conditional_formats=None, position='A1', column_totals=None, float_precision=3, column_formats=None, sparklines=None, autofilter=True)
