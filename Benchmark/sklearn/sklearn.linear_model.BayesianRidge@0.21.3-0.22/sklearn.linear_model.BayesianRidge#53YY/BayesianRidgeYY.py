from sklearn import linear_model
clf = linear_model.BayesianRidge(300,  0.001, alpha_1=1e-06, alpha_2=1e-06, lambda_1=1e-06, lambda_2=1e-06, compute_score=False, fit_intercept=True, normalize=False)
