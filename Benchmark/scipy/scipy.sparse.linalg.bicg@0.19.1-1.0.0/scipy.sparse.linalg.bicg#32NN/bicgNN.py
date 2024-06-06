import scipy
import scipy.sparse.linalg as spla
import numpy as np
A = scipy.sparse.csr_matrix(np.array([[3, 2, 0], [1, 7, 0], [0, -1, 8]]))
b = np.array([1, 2, 3])
(x, info) = spla.bicg(A, b=b, x0=None, tol=1e-06, maxiter=100, xtype=None, M=None)
