import numpy as np
from sklearn.datasets import make_friedman1
from sklearn.decomposition import MiniBatchSparsePCA
(X, _) = make_friedman1(n_samples=200, n_features=30, random_state=0)
transformer = MiniBatchSparsePCA(5, batch_size=50, callback=None, verbose=False, ridge_alpha=0.01, shuffle=True, n_iter=100, alpha=1, n_jobs=None)
