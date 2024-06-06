import plotly.express as px
df = px.data.gapminder().query("country=='Brazil'")
fig = px.line_3d(df,  'gdpPercap',  'pop',  'year',  None, line_dash=None, text=None, line_group=None, hover_name=None, hover_data=None, custom_data=None)
