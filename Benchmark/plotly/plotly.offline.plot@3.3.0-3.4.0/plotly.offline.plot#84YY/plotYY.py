import plotly.graph_objs as go
import plotly.offline as pyo
trace = go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
data = [trace]
pyo.plot(data,  True,  'Export to plot.ly',  True,  'file',  True, filename='temp-plot.html', auto_open=True, image=None, image_filename='plot_image', image_width=800, image_height=600)
