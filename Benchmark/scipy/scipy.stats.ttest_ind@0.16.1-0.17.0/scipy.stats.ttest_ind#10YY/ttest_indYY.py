import scipy.stats
result = scipy.stats.ttest_ind([1, 2, 3, 4, 5],  [2, 3, 4, 5, 6], axis=0, equal_var=True)
