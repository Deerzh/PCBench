import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df,  'year',  'lifeExp')
