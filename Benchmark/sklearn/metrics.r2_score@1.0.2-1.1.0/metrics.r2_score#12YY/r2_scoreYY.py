from sklearn.metrics import r2_score
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
r2_score(y_pred=y_pred, sample_weight=None, y_true=y_true, multioutput='uniform_average')
