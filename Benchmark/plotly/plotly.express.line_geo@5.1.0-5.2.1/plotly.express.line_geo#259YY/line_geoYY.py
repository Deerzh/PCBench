import plotly.express as px
df = px.data.gapminder().query('year == 2007')
fig = px.line_geo(df,  None,  None,  'iso_alpha',  None,  None,  None,  'continent',  None,  None,  None,  None,  0,  None,  None,  None,  None, custom_data=None, line_group=None, animation_frame=None, animation_group=None, category_orders=None)
