import pandas as pd
from pandas._testing import assert_series_equal
df1 = pd.Series({'a': 1, 'b': 1})
df2 = pd.Series({'a': 1, 'b': 1})
assert_series_equal(df1, right=df1, check_dtype=True, check_index_type='equiv')
