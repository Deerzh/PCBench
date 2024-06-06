import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada,  'year',  'pop',  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  {}, labels={}, color_discrete_sequence=None)
