import plotly.express as px
df = px.data.election()
fig = px.line_ternary(df,  'Joly',  'Coderre',  'Bergeron',  None,  None,  None, hover_name=None, hover_data=None, custom_data=None, text=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, color_discrete_sequence=None, color_discrete_map=None, line_dash_sequence=None, line_dash_map=None, line_shape=None, title=None, template=None, width=None)
