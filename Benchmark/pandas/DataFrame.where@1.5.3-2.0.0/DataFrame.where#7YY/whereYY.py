import pandas as pd
s = pd.Series(range(5))
s.where(s > 0, axis=None, inplace=False)
