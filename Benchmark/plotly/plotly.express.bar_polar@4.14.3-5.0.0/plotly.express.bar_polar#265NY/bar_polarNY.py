import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df,  'frequency',  'direction',  'strength',  None,  None,  None,  None,  None,  None,  None, labels=None, color_discrete_sequence=None, color_discrete_map=None, color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, barnorm=None, barmode='relative', direction='clockwise', start_angle=90, range_r=None)
