import polars as pl
df = pl.DataFrame({'A': [1, 2, 3, 4, 5], 'B': ['a', 'b', 'c', 'd', 'e']})
df.write_json(file='./output.json', pretty=False, row_oriented=False)
