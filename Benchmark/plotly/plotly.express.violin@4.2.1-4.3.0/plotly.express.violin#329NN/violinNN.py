import plotly.express as px
df = px.data.tips()
fig = px.violin(df,  None,  'total_bill',  None,  None,  None,  None,  None,  None,  None,  None,  {},  {},  None,  {},  'v',  'group',  False,  False,  None,  None,  None, box=False, title=None, template=None)
