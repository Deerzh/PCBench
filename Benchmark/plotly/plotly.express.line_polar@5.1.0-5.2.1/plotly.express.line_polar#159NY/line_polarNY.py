import plotly.express as px
df = px.data.wind()
fig = px.line_polar(df,  'frequency',  'direction',  'strength',  None,  None,  None,  None,  None,  None,  None,  None, category_orders=None, labels=None, color_discrete_sequence=None, color_discrete_map=None, line_dash_sequence=None)
