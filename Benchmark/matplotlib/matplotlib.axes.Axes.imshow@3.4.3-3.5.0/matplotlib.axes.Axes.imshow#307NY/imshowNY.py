import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X,  'viridis',  None,  'auto', filternorm=True, interpolation='nearest', alpha=None, vmin=None, filterrad=4.0)
