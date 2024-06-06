from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
(b, c) = (a.array, a.array)
tm.assert_extension_array_equal(b,  c,  True,  None, check_less_precise=False, check_exact=False, rtol=1e-05, atol=1e-08)
