import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df,  'total_bill',  'tip',  None,  None,  None,  None,  None,  None,  None,  {},  {},  None, range_color=None, color_continuous_midpoint=None, marginal_x=None, marginal_y=None, opacity=None, log_x=False, log_y=False)
