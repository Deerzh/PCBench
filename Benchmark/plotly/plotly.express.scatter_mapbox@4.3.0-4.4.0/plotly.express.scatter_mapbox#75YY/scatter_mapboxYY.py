import plotly.express as px
df = px.data.carshare()
fig = px.scatter_mapbox(df,  'centroid_lat',  'centroid_lon',  'peak_hour',  None,  None,  None,  None,  None,  None, animation_group=None, category_orders={})
