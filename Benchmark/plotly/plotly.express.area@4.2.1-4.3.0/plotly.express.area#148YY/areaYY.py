import plotly.express as px
df = px.data.gapminder()
fig = px.area(df,  'year',  'pop',  'country',  'continent', hover_name=None, hover_data=None, custom_data=None, text=None, facet_row=None, facet_col=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None)
