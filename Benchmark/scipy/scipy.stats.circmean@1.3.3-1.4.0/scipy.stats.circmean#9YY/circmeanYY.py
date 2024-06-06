from scipy.stats import circmean
samples = [0.1, 0.2, 6.0, 6.1]
result = circmean(samples=samples, high=6.283185307179586, low=0)
print(result)
