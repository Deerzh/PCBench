import plotly.express as px
df = px.data.gapminder()
fig = px.area(df,  'year',  'pop',  'country',  'continent',  None,  None,  None,  None,  None,  None,  None,  None,  {},  {},  None,  {},  'v',  None,  False,  False,  None,  None,  None, title=None, template=None, width=None, height=None)
