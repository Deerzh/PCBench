import plotly.express as px
df = px.data.tips()
fig = px.strip(df,  'total_bill',  'day',  None,  None,  None,  None,  None,  None,  None,  None,  {},  {},  None,  {},  'v',  'group',  False,  False,  None,  None,  None,  None, width=None, height=None)
