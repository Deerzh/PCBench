import pandas as pd
s = pd.Series([1, 2, 3])
s.set_axis(['a', 'b', 'c'], inplace=False, copy=False, axis=0)
