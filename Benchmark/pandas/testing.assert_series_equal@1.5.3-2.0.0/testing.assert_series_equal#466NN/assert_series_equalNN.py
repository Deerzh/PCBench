from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(rtol=1e-05, check_dtype=True, check_series_type=True, check_names=True, check_index_type='equiv', check_freq=True, check_exact=False, right=b, left=a, check_datetimelike_compat=False, check_index=True, check_flags=True, check_category_order=True, check_categorical=True, check_less_precise=False)
