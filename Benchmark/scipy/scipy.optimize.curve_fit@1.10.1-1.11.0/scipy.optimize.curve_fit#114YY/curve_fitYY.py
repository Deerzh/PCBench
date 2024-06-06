import numpy as np
from scipy.optimize import curve_fit

def model_function(x, a, b, c):
    return a * np.exp(-b * x) + c
xdata = np.array([0.1, 0.5, 1.0, 1.5, 2.0])
ydata = np.array([0.9, 0.6, 0.35, 0.2, 0.1])
p0 = [1.0, 1.0, 0.0]
(parameters, covariance) = curve_fit(model_function,  xdata,  ydata, p0=p0, jac=None, full_output=False, check_finite=True, absolute_sigma=False, sigma=None, method=None, bounds=(-np.inf, np.inf))
print('Estimated Parameters:', parameters)
