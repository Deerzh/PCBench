from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b,  True,  'equiv', check_freq=True, check_categorical=True, check_names=True, check_like=False, check_less_precise=False, check_datetimelike_compat=False, atol=1e-08, check_category_order=True, check_flags=True, check_exact=False, rtol=1e-05, check_series_type=True)
