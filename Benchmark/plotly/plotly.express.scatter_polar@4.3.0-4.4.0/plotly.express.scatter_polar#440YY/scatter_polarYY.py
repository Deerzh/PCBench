import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(df,  'frequency',  'direction',  None,  None,  None,  None,  None,  None,  None,  None,  None,  {},  {},  None,  {},  None,  None,  None,  None,  {},  None,  'clockwise',  90,  None, range_r=None, log_r=False, render_mode='auto', title=None)
