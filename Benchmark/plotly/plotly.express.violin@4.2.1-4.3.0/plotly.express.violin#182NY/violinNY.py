import plotly.express as px
df = px.data.tips()
fig = px.violin(df,  None,  'total_bill',  None,  None,  None,  None,  None, custom_data=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, orientation='v', violinmode='group', log_x=False)
