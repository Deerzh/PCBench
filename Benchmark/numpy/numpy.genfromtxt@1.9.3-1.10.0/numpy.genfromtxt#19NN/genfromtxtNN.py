import numpy as np
from io import StringIO
with open('/home/zhang/Packages/data2.txt', 'rb') as f:
    data = np.genfromtxt(f, dtype=float, comments='#', delimiter=',', skiprows=0)
