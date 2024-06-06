import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df,  'year',  'lifeExp',  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  {},  {},  None,  {},  None,  {},  False, log_y=False, range_x=None, range_y=None, line_shape=None, render_mode='auto', title=None)
