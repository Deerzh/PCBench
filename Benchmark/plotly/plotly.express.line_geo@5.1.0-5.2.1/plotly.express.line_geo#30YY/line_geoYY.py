import plotly.express as px
df = px.data.gapminder().query('year == 2007')
fig = px.line_geo(df,  None,  None,  'iso_alpha',  None,  None, featureidkey=None)
