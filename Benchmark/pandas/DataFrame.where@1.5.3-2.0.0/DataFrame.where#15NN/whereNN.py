import pandas as pd
s = pd.Series(range(5))
s.where(cond=s > 0, errors='raise')
