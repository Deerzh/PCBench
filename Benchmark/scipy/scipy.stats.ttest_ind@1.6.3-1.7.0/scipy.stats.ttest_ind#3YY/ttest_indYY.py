from scipy import stats
a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6]
result = stats.ttest_ind(a=a, b=b)
