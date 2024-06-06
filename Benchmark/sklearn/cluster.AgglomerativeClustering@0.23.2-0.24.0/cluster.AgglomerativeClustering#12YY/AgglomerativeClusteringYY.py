from sklearn.cluster import AgglomerativeClustering
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
clustering = AgglomerativeClustering(memory=None, affinity='euclidean', connectivity=None, linkage='ward', distance_threshold=None, compute_full_tree='auto').fit(X)
