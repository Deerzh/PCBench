import numpy as np
data = np.loadtxt(fname='data.txt', dtype=float, comments='#', delimiter=',', converters=None, skiprows=1, usecols=(0, 2), unpack=True, ndmin=1)
