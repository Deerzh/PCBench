import pandas as pd
from pandas._testing import assert_series_equal
df1 = pd.Series({'a': 1, 'b': 1})
df2 = pd.Series({'a': 1, 'b': 1})
assert_series_equal(df1,  df1,  True,  'equiv',  True,  False,  True, check_exact=False, check_datetimelike_compat=False)
