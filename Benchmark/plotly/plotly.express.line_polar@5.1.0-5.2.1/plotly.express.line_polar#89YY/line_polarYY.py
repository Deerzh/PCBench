import plotly.express as px
df = px.data.wind()
fig = px.line_polar(df,  'frequency', theta='direction', color='strength', line_dash=None, hover_name=None, hover_data=None, custom_data=None, line_group=None, text=None, animation_frame=None, animation_group=None)
