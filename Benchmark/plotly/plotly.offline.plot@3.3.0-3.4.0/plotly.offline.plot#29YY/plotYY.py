import plotly.graph_objs as go
import plotly.offline as pyo
trace = go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
data = [trace]
pyo.plot(data,  True,  'Export to plot.ly',  True,  'file',  True, filename='temp-plot.html')
