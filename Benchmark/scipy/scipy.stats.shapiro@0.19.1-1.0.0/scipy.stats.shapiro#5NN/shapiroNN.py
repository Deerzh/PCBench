from scipy import stats
x = [1, 2, 3, 4, 5]
(statistic, p_value) = stats.shapiro(x=x, a=None)
