import scipy.signal
num = [1]
den = [1, -0.5, 0.25]
(group_delay, _) = scipy.signal.group_delay((num, den), w=512)
