from sklearn.cluster import SpectralClustering
import numpy as np
X = np.array([[1, 1], [2, 1], [1, 0], [4, 7], [3, 5], [3, 6]])
clustering = SpectralClustering(5,  None,  None,  10,  1.0,  'rbf', n_neighbors=10, eigen_tol=0.0, assign_labels='kmeans', degree=3, coef0=1, kernel_params=None, n_jobs=None).fit(X)
