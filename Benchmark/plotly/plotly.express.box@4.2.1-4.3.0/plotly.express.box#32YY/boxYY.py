import plotly.express as px
df = px.data.tips()
fig = px.box(df,  'time',  'total_bill',  None, facet_row=None, facet_col=None, hover_name=None)
