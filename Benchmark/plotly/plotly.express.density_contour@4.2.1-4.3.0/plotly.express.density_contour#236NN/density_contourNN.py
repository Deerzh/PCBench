import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df,  'total_bill',  'tip',  None,  None,  None,  None,  None,  None,  None,  None,  {},  {},  None,  {},  None,  None, trendline=None, trendline_color_override=None, log_x=False, log_y=False)
