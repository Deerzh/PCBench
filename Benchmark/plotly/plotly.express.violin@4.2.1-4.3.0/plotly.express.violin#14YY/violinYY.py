import plotly.express as px
df = px.data.tips()
fig = px.violin(df, x=None, y='total_bill', color=None)
