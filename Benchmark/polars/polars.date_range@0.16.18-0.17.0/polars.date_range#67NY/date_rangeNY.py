import polars as pl
from datetime import date
pl.date_range(closed='both', interval='1mo', low=date(2022, 1, 1), lazy=False, high=date(2022, 3, 1))
