import numpy as np
from scipy.fft import rfft
x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
result = rfft(x,  8, axis=-1, norm=None, overwrite_x=False, workers=None)
