import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X,  'viridis',  None,  'auto',  'nearest',  None, extent=None, origin='upper', filterrad=4.0, vmin=None, vmax=None, filternorm=True)
