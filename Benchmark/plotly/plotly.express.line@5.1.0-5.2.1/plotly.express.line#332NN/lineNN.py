import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df,  'year',  'lifeExp',  None,  None,  None,  None,  None,  None,  None,  None,  None,  0,  None,  None,  None,  None, error_y=None, error_y_minus=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, orientation=None, color_discrete_sequence=None)
