import plotly.express as px
df = px.data.election()
fig = px.line_ternary(df,  'Joly', b='Coderre', c='Bergeron', color=None, line_dash=None, line_group=None, hover_name=None)
