import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes,  explode,  labels,  colors,  '%1.1f%%', counterclock=False, startangle=90, data=None, shadow=True, pctdistance=0.85, labeldistance=1.05, radius=False)
