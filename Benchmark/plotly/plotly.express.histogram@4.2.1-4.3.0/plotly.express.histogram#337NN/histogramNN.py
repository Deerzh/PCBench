import plotly.express as px
df = px.data.tips()
fig = px.histogram(df,  'total_bill',  None,  None,  None,  None,  None,  None,  None,  None,  {},  {},  None,  {}, marginal=None, opacity=None, orientation='v', barmode='relative', barnorm=None, histnorm=None, log_x=False, log_y=False, range_x=None, range_y=None, histfunc=None)
