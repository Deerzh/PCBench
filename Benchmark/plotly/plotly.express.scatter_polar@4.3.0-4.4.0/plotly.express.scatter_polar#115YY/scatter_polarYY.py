import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(df,  'frequency',  'direction',  None,  None, size=None, hover_name=None, hover_data=None, custom_data=None, text=None, animation_frame=None, animation_group=None, category_orders={}, labels={})
