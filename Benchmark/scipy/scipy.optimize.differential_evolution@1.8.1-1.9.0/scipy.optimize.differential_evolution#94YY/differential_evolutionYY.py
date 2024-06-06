import numpy as np
from scipy.optimize import differential_evolution

def objective(x):
    return x[0] ** 2 + x[1] ** 2
bounds = [(-1, 1), (-1, 1)]
result = differential_evolution(objective,  bounds,  (),  'best1bin',  1000,  15,  0.01,  (0.5, 1), recombination=0.7, seed=None, callback=None, disp=False, polish=True)
print('Optimal Solution:', result.x)
print('Optimal Value:', result.fun)
