import numpy as np
a = np.array([[1, 2, np.nan], [4, np.nan, 6]])
result = np.nanmin(a, axis=1, out=None)
