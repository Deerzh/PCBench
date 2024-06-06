from pandas.testing import assert_frame_equal
import pandas as pd
df1 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
df2 = pd.DataFrame({'a': [1, 2], 'b': [3.0, 4.0]})
assert_frame_equal(left=df1, right=df1, check_dtype=True)
