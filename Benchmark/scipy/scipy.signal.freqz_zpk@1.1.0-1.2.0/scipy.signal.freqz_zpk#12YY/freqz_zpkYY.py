import scipy.signal
z = [0.5 + 0.5j, 0.5 - 0.5j]
p = [0.2, 0.3]
k = 2.0
worN = 256
whole = False
(w, h) = scipy.signal.freqz_zpk(z,  p,  k, worN=worN, whole=whole)
