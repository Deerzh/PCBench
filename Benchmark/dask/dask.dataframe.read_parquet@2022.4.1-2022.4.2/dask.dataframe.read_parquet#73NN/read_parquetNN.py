import dask.dataframe as dd
ddf = dd.read_parquet('./example.parquet',  None,  None,  None, index=None, storage_options=None, engine='auto', gather_statistics=None, ignore_metadata_file=False, metadata_task_size=None, split_row_groups=None)
