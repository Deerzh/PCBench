import numpy as np
result = np.nanprod(a=[1, 2, np.nan, 4], axis=0, dtype=int, out=None)
