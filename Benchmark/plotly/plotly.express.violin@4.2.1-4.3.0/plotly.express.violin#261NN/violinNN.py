import plotly.express as px
df = px.data.tips()
fig = px.violin(df,  None,  'total_bill',  None,  None,  None,  None,  None,  None,  None,  None,  {},  {},  None,  {}, orientation='v', violinmode='group', log_x=False, log_y=False, range_x=None, range_y=None, points=None)
