from sklearn import linear_model
clf = linear_model.ElasticNet(1.0,  0.5,  True,  False,  'auto',  1000, copy_X=True, tol=0.0001, warm_start=False)
