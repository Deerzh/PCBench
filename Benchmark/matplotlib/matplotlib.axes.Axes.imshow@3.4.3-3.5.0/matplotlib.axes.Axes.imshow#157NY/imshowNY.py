import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X,  'viridis',  None,  'auto', filternorm=True, filterrad=4.0, interpolation='nearest')
