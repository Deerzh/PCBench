import numpy as np
from sklearn.datasets import make_sparse_coded_signal
from sklearn.decomposition import MiniBatchDictionaryLearning
(X, dictionary, code) = make_sparse_coded_signal(n_samples=100, n_components=15, n_features=20, n_nonzero_coefs=10, random_state=42)
dict_learner = MiniBatchDictionaryLearning(batch_size=3, transform_algorithm='omp', dict_init=None, transform_alpha=None, split_sign=False, n_components=None, n_jobs=None, n_iter=1000, fit_algorithm='lars', transform_n_nonzero_coefs=None, shuffle=True, verbose=False, random_state=None, alpha=1)
