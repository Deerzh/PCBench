from scipy.optimize import basinhopping

def objective(x):
    return (x[0] - 2) ** 2 + (x[1] - 3) ** 2
x0 = [0.0, 0.0]
minimizer_kwargs = {'method': 'L-BFGS-B', 'bounds': [(-1, 4), (-1, 4)]}
result = basinhopping(func=objective, x0=x0)
print('Optimal value:', result.fun)
print('Optimal solution:', result.x)
