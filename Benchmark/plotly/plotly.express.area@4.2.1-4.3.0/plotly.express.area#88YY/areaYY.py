import plotly.express as px
df = px.data.gapminder()
fig = px.area(df,  'year',  'pop', line_group='country', color='continent', hover_name=None, hover_data=None, custom_data=None, text=None, facet_row=None, facet_col=None, animation_frame=None)
