import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df,  'frequency',  'direction',  'strength',  None,  None,  None,  None,  None,  {},  {},  None,  {},  None,  'relative',  'clockwise',  90,  None,  False,  None, template=None)
