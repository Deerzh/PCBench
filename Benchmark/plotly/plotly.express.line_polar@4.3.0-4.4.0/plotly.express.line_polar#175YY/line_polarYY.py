import plotly.express as px
df = px.data.wind()
fig = px.line_polar(df,  'frequency',  'direction',  'strength',  None,  None,  None,  None,  None,  None,  None,  None,  {},  {},  None, color_discrete_map={}, line_dash_sequence=None, line_dash_map={})
