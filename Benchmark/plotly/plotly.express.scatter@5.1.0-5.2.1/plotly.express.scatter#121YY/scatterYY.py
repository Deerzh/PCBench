import plotly.express as px
df = px.data.iris()
fig = px.scatter(df,  'sepal_width',  'sepal_length',  None,  None,  None,  None,  None,  None,  None,  None,  None,  0, facet_row_spacing=None, facet_col_spacing=None)
