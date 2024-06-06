import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(data_frame=df, r='frequency', theta='direction', color=None, symbol=None, size=None, hover_name=None, hover_data=None, custom_data=None, text=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, symbol_sequence=None, symbol_map={}, opacity=None, direction='clockwise', start_angle=90, size_max=None, range_r=None, log_r=False, render_mode='auto', title=None)
