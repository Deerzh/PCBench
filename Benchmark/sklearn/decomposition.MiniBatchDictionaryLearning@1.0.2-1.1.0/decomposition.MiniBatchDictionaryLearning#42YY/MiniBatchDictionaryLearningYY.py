import numpy as np
from sklearn.datasets import make_sparse_coded_signal
from sklearn.decomposition import MiniBatchDictionaryLearning
(X, dictionary, code) = make_sparse_coded_signal(n_samples=100, n_components=15, n_features=20, n_nonzero_coefs=10, random_state=42)
dict_learner = MiniBatchDictionaryLearning(None, transform_n_nonzero_coefs=None)
