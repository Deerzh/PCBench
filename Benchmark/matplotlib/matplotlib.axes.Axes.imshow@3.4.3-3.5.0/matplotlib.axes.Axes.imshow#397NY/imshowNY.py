import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X,  'viridis',  None,  'auto', interpolation='nearest', filterrad=4.0, vmax=None, alpha=None, filternorm=True, vmin=None)
