import plotly.express as px
df = px.data.tips()
fig = px.violin(df,  None,  'total_bill',  None, facet_row=None)
