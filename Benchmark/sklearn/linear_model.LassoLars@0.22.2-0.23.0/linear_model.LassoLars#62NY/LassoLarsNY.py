from sklearn import linear_model
reg = linear_model.LassoLars(1.0,  True,  False,  True, precompute='auto', max_iter=500, eps=2.220446049250313e-16, copy_X=True, fit_path=True, positive=False)
