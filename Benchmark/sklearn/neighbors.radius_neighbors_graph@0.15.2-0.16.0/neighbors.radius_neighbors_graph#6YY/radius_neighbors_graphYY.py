from sklearn.neighbors import radius_neighbors_graph
X = [[0], [3], [1]]
A = radius_neighbors_graph(X, radius=1.5, mode='connectivity')
