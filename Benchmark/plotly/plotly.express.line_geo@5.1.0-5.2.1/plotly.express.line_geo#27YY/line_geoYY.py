import plotly.express as px
df = px.data.gapminder().query('year == 2007')
fig = px.line_geo(df, lat=None, lon=None, locations='iso_alpha', locationmode=None, geojson=None)
