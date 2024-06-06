import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes,  explode, wedgeprops={'edgecolor': 'black'}, labels=labels, data=None, radius=False, pctdistance=0.85, labeldistance=1.05, autopct='%1.1f%%', startangle=90, colors=colors, textprops={'color': 'white'}, shadow=True, center=(0, 0), counterclock=False)
