import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
max_value = np.max(a,  None,  None, keepdims=False, initial=-np.inf)
print(max_value)
