import dask.dataframe as dd
ddf = dd.read_parquet('./example.parquet',  None,  None,  None,  None,  None,  'auto',  None, ignore_metadata_file=False)
