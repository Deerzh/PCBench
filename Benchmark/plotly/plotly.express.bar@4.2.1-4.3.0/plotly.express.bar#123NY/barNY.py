import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada,  'year',  'pop',  None,  None,  None,  None,  None,  None,  None,  None,  None,  None, error_y_minus=None, animation_frame=None)
