from pandas import testing as tm
import pandas as pd
a = pd.Index([1, 2, 3])
b = pd.Index([1, 2, 3])
tm.assert_index_equal(a, right=b, exact='equiv', check_names=True, check_less_precise=False, check_exact=True, check_categorical=True, check_order=True, rtol=1e-05, atol=1e-08, obj='Index')
