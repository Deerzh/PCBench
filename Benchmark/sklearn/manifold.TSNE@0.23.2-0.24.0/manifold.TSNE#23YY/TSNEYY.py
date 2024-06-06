import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(perplexity=30.0, min_grad_norm=1e-07, learning_rate=200.0, n_iter=1000, random_state=None, early_exaggeration=12.0, init='random', verbose=0, n_iter_without_progress=300, metric='euclidean').fit_transform(X)
