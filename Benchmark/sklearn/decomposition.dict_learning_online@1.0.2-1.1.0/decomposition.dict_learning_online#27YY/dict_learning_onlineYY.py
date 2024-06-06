from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, n_iter=100, n_jobs=None, batch_size=3, alpha=1, callback=None, verbose=False, return_code=True, dict_init=None, shuffle=True)
