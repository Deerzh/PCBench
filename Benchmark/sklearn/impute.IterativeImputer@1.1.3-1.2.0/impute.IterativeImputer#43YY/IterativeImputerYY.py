import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(None, tol=0.001, max_iter=10, sample_posterior=False, missing_values=0)
