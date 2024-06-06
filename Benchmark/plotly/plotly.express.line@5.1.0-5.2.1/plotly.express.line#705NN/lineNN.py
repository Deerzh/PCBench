import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df,  'year',  'lifeExp',  None,  None,  None,  None,  None,  None,  None,  None,  None,  0,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  False,  False,  None,  None,  None,  'auto', title=None, template=None, width=None)
