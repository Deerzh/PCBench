import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df,  'total_bill',  'tip',  None,  None,  None, facet_col=None, hover_name=None, hover_data=None, animation_frame=None)
