from sklearn.neighbors import kneighbors_graph
X = [[0], [3], [1]]
A = kneighbors_graph(X,  2, mode='connectivity')
