import plotly.express as px
df = px.data.gapminder().query("country=='Brazil'")
fig = px.line_3d(df,  'gdpPercap', y='pop')
