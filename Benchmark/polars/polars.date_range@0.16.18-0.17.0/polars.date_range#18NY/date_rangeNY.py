import polars as pl
from datetime import date
pl.date_range(date(2022, 1, 1), name=None, high=date(2022, 3, 1), closed='both', lazy=False)
