import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = np.nanstd(a,  0, dtype=float, out=None, ddof=1, keepdims=False)
