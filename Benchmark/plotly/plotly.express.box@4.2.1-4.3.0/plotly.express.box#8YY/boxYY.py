import plotly.express as px
df = px.data.tips()
fig = px.box(df,  'time', y='total_bill')
