import plotly.express as px
df = px.data.tips()
fig = px.histogram(df,  'total_bill',  None, color=None, facet_row=None)
