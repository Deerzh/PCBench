from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(check_exact=False, check_dtype=True, check_index_type='equiv', check_index=True, check_less_precise=False, check_names=True, left=a, check_series_type=True, right=b)
