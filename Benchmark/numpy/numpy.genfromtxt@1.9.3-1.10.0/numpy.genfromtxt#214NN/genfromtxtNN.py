import numpy as np
from io import StringIO
with open('data2.txt', 'rb') as f:
    data = np.genfromtxt(f,  float,  '#',  ',',  0,  0,  0,  None,  '',  None,  None,  None,  None,  None,  None,  '_', autostrip=False, case_sensitive=True, defaultfmt='f%i', unpack=None)
