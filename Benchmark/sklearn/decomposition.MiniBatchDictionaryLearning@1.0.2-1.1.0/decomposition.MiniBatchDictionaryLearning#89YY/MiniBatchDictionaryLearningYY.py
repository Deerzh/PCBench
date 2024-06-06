import numpy as np
from sklearn.datasets import make_sparse_coded_signal
from sklearn.decomposition import MiniBatchDictionaryLearning
(X, dictionary, code) = make_sparse_coded_signal(n_samples=100, n_components=15, n_features=20, n_nonzero_coefs=10, random_state=42)
dict_learner = MiniBatchDictionaryLearning(transform_algorithm='omp', n_iter=1000, alpha=1, fit_algorithm='lars', shuffle=True, batch_size=3, n_components=None, transform_n_nonzero_coefs=None, dict_init=None, n_jobs=None)
