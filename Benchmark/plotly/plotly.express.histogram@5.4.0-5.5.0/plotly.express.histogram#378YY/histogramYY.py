import plotly.express as px
df = px.data.tips()
fig = px.histogram(df,  'total_bill',  None,  None,  None,  None,  None,  0,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  'relative',  None,  None, log_x=False)
