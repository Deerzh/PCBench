import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X,  'viridis',  None,  'auto', filterrad=4.0, resample=None, url=None, alpha=None, interpolation='nearest', filternorm=True)
