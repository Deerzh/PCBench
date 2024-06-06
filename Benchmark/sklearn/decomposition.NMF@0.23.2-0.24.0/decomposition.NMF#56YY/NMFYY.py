import numpy as np
X = np.array([[1, 1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]])
from sklearn.decomposition import NMF
model = NMF(init='random', n_components=2, solver='cd', tol=0.0001, max_iter=200, beta_loss='frobenius', random_state=0)
