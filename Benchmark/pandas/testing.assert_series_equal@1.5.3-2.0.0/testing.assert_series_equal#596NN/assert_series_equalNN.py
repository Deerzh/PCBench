from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a, rtol=1e-05, right=b, check_less_precise=False, check_names=True, check_like=False, check_dtype=True, check_index=True, obj='Series', check_datetimelike_compat=False, atol=1e-08, check_categorical=True, check_flags=True, check_category_order=True, check_freq=True, check_exact=False, check_index_type='equiv', check_series_type=True)
