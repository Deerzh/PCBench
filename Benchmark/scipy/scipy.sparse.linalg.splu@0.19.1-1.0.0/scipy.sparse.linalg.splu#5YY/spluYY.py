from scipy.sparse import csc_matrix
from scipy.sparse.linalg import splu
A = csc_matrix([[1, 2, 0], [3, 4, 0], [0, 5, 6]])
lu = splu(A=A, permc_spec='MMD_AT_PLUS_A')
