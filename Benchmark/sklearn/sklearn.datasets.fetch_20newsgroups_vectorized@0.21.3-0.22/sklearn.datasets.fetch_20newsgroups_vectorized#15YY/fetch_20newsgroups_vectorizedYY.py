from sklearn.datasets import fetch_20newsgroups_vectorized
newsgroups_train = fetch_20newsgroups_vectorized(subset='train', remove=(), data_home='/home/zhang/sklearn_data', download_if_missing=True)
