import pandas as pd
idx = pd.Index(list('abcd'))
idx.slice_indexer('b', end='c', step=None)
