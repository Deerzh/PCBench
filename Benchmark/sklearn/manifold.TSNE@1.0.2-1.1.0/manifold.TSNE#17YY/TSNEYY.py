import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(perplexity=30.0, learning_rate='warn', early_exaggeration=12.0).fit_transform(X)
