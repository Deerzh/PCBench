import scipy.signal
sos = [[1, 0, -1, 1, -1.5610180758007186, 0.6413520164758281], [1, 0, -1, 1, -1.7819866770370927, 0.7969173664141453]]
(freq, response) = scipy.signal.sosfreqz(sos, worN=200, whole=True)
