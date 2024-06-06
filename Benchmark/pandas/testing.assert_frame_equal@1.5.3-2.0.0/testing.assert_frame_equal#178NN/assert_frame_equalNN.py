from pandas.testing import assert_frame_equal
import pandas as pd
df1 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
df2 = pd.DataFrame({'a': [1, 2], 'b': [3.0, 4.0]})
assert_frame_equal(df1,  df1,  True,  'equiv',  'equiv',  True,  False,  True,  False, check_exact=False, check_datetimelike_compat=False, check_categorical=True, check_like=False, check_freq=True, check_flags=True, rtol=1e-05, atol=1e-08, obj='DataFrame')
