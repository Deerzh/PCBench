from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b, check_dtype=True, check_names=True, check_less_precise=False, check_index_type='equiv', check_flags=True, atol=1e-08, check_freq=True, check_like=False, check_categorical=True, check_category_order=True, check_exact=False, rtol=1e-05, check_index=True, check_series_type=True, check_datetimelike_compat=False)
