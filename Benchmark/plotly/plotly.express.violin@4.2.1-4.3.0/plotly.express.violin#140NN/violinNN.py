import plotly.express as px
df = px.data.tips()
fig = px.violin(df,  None,  'total_bill',  None,  None,  None,  None,  None,  None,  None,  None,  {},  {}, color_discrete_sequence=None, color_discrete_map={}, orientation='v')
