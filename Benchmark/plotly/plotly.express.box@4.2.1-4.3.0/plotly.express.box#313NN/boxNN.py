import plotly.express as px
df = px.data.tips()
fig = px.box(df,  'time',  'total_bill',  None,  None,  None,  None,  None,  None,  None,  None,  {}, labels={}, color_discrete_sequence=None, color_discrete_map={}, orientation='v', boxmode='group', log_x=False, log_y=False, range_x=None, range_y=None, points=None, notched=False, title=None)
