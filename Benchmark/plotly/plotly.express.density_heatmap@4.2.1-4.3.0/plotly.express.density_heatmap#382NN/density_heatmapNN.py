import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df,  'total_bill',  'tip',  None,  None,  None,  None,  None,  None,  None,  {},  {},  None,  None,  None,  None,  None,  None,  False,  False,  None,  None,  None,  None, nbinsx=None, nbinsy=None, title=None)
