import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df,  'frequency',  'direction',  'strength',  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None, range_color=None, color_continuous_midpoint=None, barnorm=None, barmode='relative', direction='clockwise')
