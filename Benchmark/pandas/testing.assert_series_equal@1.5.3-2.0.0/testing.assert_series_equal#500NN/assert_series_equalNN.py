from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b,  True,  'equiv',  True,  False,  True,  False, check_flags=True, atol=1e-08, check_like=False, check_categorical=True, check_index=True, rtol=1e-05, check_category_order=True, check_datetimelike_compat=False, check_freq=True)
