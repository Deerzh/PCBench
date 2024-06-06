import plotly.express as px
df = px.data.gapminder()
fig = px.area(df,  'year',  'pop',  'country',  'continent',  None,  None,  None,  None,  None,  None,  None,  None,  {},  {},  None,  {},  'v',  None, log_x=False, log_y=False, range_x=None, range_y=None, line_shape=None, title=None)
