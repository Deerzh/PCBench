import numpy as np
data = np.loadtxt('./data.txt',  float,  '#',  ',',  None,  1, usecols=(0, 2), unpack=True, ndmin=1)
