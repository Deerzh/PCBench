import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(df,  'frequency',  'direction',  None,  None,  None,  None,  None,  None, text=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, color_continuous_scale=None, range_color=None, color_continuous_midpoint=None)
