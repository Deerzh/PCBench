import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df,  'year',  'lifeExp',  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  {},  {},  None,  {},  None,  {},  False,  False,  None,  None,  None, render_mode='auto', title=None, template=None, width=None, height=None)
