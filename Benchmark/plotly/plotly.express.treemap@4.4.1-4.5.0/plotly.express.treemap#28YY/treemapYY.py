import plotly.express as px
df = px.data.tips()
fig = px.treemap(data_frame=df, names=None, values='total_bill', parents=None, ids=None, color=None)
