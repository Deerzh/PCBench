import plotly.express as px
df = px.data.gapminder().query("country=='Brazil'")
fig = px.line_3d(df,  'gdpPercap',  'pop',  'year',  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None, line_dash_map=None)
