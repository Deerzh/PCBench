from sklearn import linear_model
reg = linear_model.Lars(True,  False, normalize=True, precompute='auto', n_nonzero_coefs=500)
