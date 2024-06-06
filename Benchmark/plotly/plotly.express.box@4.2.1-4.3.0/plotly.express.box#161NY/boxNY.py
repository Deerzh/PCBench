import plotly.express as px
df = px.data.tips()
fig = px.box(df,  'time',  'total_bill',  None,  None,  None,  None,  None,  None,  None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, orientation='v', boxmode='group')
