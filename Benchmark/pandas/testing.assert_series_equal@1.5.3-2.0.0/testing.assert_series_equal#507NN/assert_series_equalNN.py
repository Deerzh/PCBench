from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b,  True,  'equiv',  True,  False, rtol=1e-05, atol=1e-08, check_like=False, check_datetimelike_compat=False, check_category_order=True, check_categorical=True, check_names=True, check_exact=False, check_flags=True, check_freq=True)
