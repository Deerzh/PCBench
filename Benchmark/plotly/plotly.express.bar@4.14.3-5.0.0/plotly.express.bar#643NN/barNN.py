import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada,  'year',  'pop',  None,  None,  None,  0,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None, labels=None, color_discrete_sequence=None, color_discrete_map=None, color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, opacity=None, orientation=None, barmode='relative', log_x=False, log_y=False, range_x=None, range_y=None, title=None)
