import numpy as np
from scipy.optimize import differential_evolution

def objective(x):
    return x[0] ** 2 + x[1] ** 2
bounds = [(-1, 1), (-1, 1)]
result = differential_evolution(objective,  bounds,  (),  'best1bin', maxiter=1000, popsize=15)
print('Optimal Solution:', result.x)
print('Optimal Value:', result.fun)
