from sklearn.metrics import classification_report
y_true = [0, 1, 2, 2, 2]
y_pred = [0, 0, 2, 2, 1]
target_names = ['class 0', 'class 1', 'class 2']
classification_report(y_true=y_true, y_pred=y_pred, labels=None, target_names=target_names, sample_weight=None)
