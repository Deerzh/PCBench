import plotly.express as px
df = px.data.iris()
fig = px.scatter(df,  'sepal_width',  'sepal_length',  None,  None,  None,  None,  None,  None,  None,  None,  None, error_x=None, error_x_minus=None, error_y=None)
