import numpy as np
from scipy.optimize import shgo

def func(x):
    return x[0] * x[1] * x[2]
bounds = [(1, 5), (1, 5), (1, 5)]
result = shgo(func,  bounds, args=(), constraints=None, n=None)
print(result.fun)
