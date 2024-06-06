import plotly.graph_objs as go
import plotly.offline as pyo
trace = go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
data = [trace]
pyo.plot(data,  False,  'Export to plot.ly',  True,  'file',  True,  'temp-plot.html',  True,  None,  'plot_image',  800,  600, config=None, include_mathjax=False, auto_play=True)
