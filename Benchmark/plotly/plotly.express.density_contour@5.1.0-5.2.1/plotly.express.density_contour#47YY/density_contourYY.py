import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df,  'total_bill',  'tip',  None,  None,  None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None)
