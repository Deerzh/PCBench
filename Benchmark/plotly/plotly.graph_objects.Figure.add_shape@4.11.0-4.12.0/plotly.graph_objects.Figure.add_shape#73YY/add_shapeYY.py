import plotly.graph_objects as go
fig = go.Figure()
trace1 = go.Bar(x=[1, 2, 3], y=[4, 5, 6], name='Bar Trace')
fig.add_trace(trace1)
fig.add_shape(None,  None,  None,  None,  None, line=dict(color='FireBrick', width=3), name=None, opacity=None, path=None, templateitemname=None, type='line')
