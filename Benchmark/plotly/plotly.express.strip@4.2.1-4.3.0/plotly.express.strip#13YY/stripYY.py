import plotly.express as px
df = px.data.tips()
fig = px.strip(df,  'total_bill', y='day', color=None)
