import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(data=None, explode=explode, startangle=90, x=sizes, colors=colors, autopct='%1.1f%%', labeldistance=1.05, shadow=True, pctdistance=0.85, labels=labels, radius=False)
