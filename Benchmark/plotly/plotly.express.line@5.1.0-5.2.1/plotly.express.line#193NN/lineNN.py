import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df,  'year',  'lifeExp',  None,  None,  None,  None,  None,  None,  None,  None,  None,  0,  None,  None, error_x=None, error_x_minus=None, error_y=None, error_y_minus=None)
