import numpy as np
from sklearn.datasets import make_sparse_coded_signal
from sklearn.decomposition import DictionaryLearning
(X, dictionary, code) = make_sparse_coded_signal(n_samples=100, n_components=15, n_features=20, n_nonzero_coefs=10, random_state=42, data_transposed=False)
dict_learner = DictionaryLearning(tol=1e-08, fit_algorithm='lars', alpha=1, transform_n_nonzero_coefs=None, max_iter=1000, transform_alpha=None, transform_algorithm='omp', n_jobs=None)
