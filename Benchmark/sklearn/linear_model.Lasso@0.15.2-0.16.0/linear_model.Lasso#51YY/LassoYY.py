from sklearn import linear_model
clf = linear_model.Lasso(1.0,  True,  False,  'auto', copy_X=True, max_iter=1000, tol=0.0001, warm_start=False, positive=False)
