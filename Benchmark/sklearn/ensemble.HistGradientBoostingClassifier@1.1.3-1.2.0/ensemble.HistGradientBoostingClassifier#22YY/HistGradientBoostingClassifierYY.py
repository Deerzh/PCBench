from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(min_samples_leaf=20, max_depth=None, learning_rate=0.1, max_leaf_nodes=31, max_iter=100)
