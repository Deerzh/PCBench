import scipy.linalg
a = [[2, 1], [5, 3]]
b = [1, 2]
x = scipy.linalg.solve(a,  b,  False,  False,  False,  False, check_finite=True, assume_a='gen', transposed=False)
