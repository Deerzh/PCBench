from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X,  2, n_jobs=None, alpha=1, dict_init=None, batch_size=3, random_state=None, return_inner_stats=False, callback=None, method='lars', return_code=True, return_n_iter=False, verbose=False, inner_stats=None, n_iter=100, shuffle=True, iter_offset=0)
