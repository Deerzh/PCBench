from sklearn import linear_model
reg = linear_model.LassoLars(1.0,  True, verbose=False, normalize=True, precompute='auto', max_iter=500)
