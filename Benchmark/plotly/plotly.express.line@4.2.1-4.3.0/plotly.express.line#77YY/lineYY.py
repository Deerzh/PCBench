import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x='year', y='lifeExp', line_group=None, color=None, line_dash=None, hover_name=None, hover_data=None, custom_data=None, text=None, facet_row=None)
