import polars as pl
df = pl.DataFrame({'date_str': ['2021-01-01', '2021-02-01', '2021-03-01']})
a = pl.col('date_str')
a.str.strptime(pl.Date, format=None, tz_aware=False, cache=True, exact=True, strict=True, utc=False)
