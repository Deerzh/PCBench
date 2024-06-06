import numpy as np
from scipy.linalg import eigh
a = np.array([[4, 1, 2], [1, 3, 1], [2, 1, 4]])
b = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
(eigenvalues, eigenvectors) = eigh(a,  b,  True,  False, overwrite_a=False, overwrite_b=False)
