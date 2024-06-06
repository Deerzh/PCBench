import plotly.express as px
df = px.data.gapminder().query('year == 2007')
fig = px.line_geo(df,  None,  None,  'iso_alpha',  None,  None,  None,  'continent',  None, text=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None)
