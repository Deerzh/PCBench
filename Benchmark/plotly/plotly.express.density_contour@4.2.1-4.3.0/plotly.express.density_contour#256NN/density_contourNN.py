import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df,  'total_bill',  'tip',  None,  None,  None,  None,  None,  None,  None,  None,  {},  {},  None,  {},  None,  None,  None,  None,  False, log_y=False, range_x=None)
