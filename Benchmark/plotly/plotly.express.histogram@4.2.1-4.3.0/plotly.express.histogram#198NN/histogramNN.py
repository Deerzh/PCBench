import plotly.express as px
df = px.data.tips()
fig = px.histogram(df,  'total_bill',  None,  None,  None,  None,  None,  None,  None,  None,  {},  {}, color_discrete_sequence=None, color_discrete_map={}, marginal=None, opacity=None, orientation='v', barmode='relative', barnorm=None)
