import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x,  None,  ['A', 'B', 'C', 'D'],  None,  '%1.1f%%', shadow=False, labeldistance=1.1, pctdistance=0.6, normalize=True)
