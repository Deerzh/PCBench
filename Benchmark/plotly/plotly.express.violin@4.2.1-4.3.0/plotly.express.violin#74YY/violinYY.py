import plotly.express as px
df = px.data.tips()
fig = px.violin(df,  None,  'total_bill',  None, facet_row=None, facet_col=None, hover_name=None, hover_data=None, custom_data=None, animation_frame=None, animation_group=None)
