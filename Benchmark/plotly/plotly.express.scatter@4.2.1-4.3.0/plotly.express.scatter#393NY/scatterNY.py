import plotly.express as px
df = px.data.iris()
fig = px.scatter(df,  'sepal_width',  'sepal_length',  None,  None,  None,  None,  None,  None,  None,  None,  None,  None, error_x_minus=None, error_y=None, error_y_minus=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, symbol_sequence=None, symbol_map={})
