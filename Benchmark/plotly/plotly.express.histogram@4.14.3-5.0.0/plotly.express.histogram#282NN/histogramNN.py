import plotly.express as px
df = px.data.tips()
fig = px.histogram(df,  'total_bill',  None,  None,  None,  None,  0,  None,  None,  None,  None,  None,  None,  None,  None,  None, color_discrete_map=None, marginal=None, opacity=None, orientation=None, barmode='relative', barnorm=None, histnorm=None)
