import scipy.signal
wp = 0.1
ws = 0.2
gpass = 2
gstop = 40
analog = False
scipy.signal.cheb2ord(wp=wp, ws=ws, gpass=gpass, gstop=gstop, analog=analog)
