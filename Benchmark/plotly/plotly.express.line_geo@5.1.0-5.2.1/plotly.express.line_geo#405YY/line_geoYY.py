import plotly.express as px
df = px.data.gapminder().query('year == 2007')
fig = px.line_geo(df, lat=None, lon=None, locations='iso_alpha', locationmode=None, geojson=None, featureidkey=None, color='continent', line_dash=None, text=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, hover_name=None, hover_data=None, custom_data=None, line_group=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, color_discrete_sequence=None, color_discrete_map=None, line_dash_sequence=None, line_dash_map=None)
