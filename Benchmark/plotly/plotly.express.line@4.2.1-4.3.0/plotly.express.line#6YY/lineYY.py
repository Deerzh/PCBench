import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(data_frame=df, x='year')
