import plotly.express as px
df = px.data.tips()
fig = px.strip(df,  'total_bill',  'day',  None,  None,  None,  None,  None,  None,  None,  None,  {},  {},  None,  {},  'v',  'group', log_x=False, log_y=False, range_x=None)
