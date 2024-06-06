from scipy.optimize import dual_annealing

def objective(x):
    return x[0] ** 2 + x[1] ** 2
bounds = [(-1, 1), (-1, 1)]
maxiter = 1000
initial_temp = 5230.0
restart_temp_ratio = 2e-05
visit = 2.62
accept = -5.0
maxfun = 10000000.0
result = dual_annealing(objective,  bounds,  (),  maxiter,  None,  initial_temp,  restart_temp_ratio,  visit, accept=accept, maxfun=maxfun, seed=None)
print('Optimal solution:', result.x)
print('Optimal value:', result.fun)
