import plotly.express as px
df = px.data.tips()
fig = px.histogram(df,  'total_bill',  None,  None,  None,  None,  None,  0,  None,  None,  None, hover_data=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, color_discrete_sequence=None, color_discrete_map=None, pattern_shape_sequence=None, pattern_shape_map=None, marginal=None, opacity=None, orientation=None, barmode='relative', barnorm=None)
