import scipy.signal
taps = scipy.signal.firwin(30,  0.3,  0.05,  'hamming',  True,  True,  1.0)
