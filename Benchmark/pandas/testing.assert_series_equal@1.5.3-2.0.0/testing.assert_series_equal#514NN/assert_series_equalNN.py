from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b,  True,  'equiv', check_datetimelike_compat=False, check_categorical=True, check_less_precise=False, check_exact=False, check_index=True, check_names=True, check_flags=True, check_freq=True, check_series_type=True, check_category_order=True, rtol=1e-05, atol=1e-08)
