import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, x='total_bill', y='tip')
