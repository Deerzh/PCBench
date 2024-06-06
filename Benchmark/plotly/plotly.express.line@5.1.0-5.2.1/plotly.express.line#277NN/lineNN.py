import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df,  'year',  'lifeExp',  None,  None,  None,  None,  None,  None,  None,  None,  None,  0,  None,  None,  None,  None,  None,  None,  None,  None, category_orders=None, labels=None)
