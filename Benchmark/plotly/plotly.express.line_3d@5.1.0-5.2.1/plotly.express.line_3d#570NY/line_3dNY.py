import plotly.express as px
df = px.data.gapminder().query("country=='Brazil'")
fig = px.line_3d(df,  'gdpPercap',  'pop',  'year',  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None, log_x=False, log_y=False, log_z=False, range_x=None, range_y=None, range_z=None, title=None, template=None)
