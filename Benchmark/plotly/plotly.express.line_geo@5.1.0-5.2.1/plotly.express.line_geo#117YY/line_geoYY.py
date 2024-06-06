import plotly.express as px
df = px.data.gapminder().query('year == 2007')
fig = px.line_geo(df,  None,  None, locations='iso_alpha', locationmode=None, geojson=None, featureidkey=None, color='continent', line_dash=None, text=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None)
