import plotly.express as px
df = px.data.carshare()
fig = px.scatter_mapbox(df,  'centroid_lat',  'centroid_lon',  'peak_hour',  None,  None,  None,  None,  None,  None,  None,  {},  {},  None,  {},  None,  None, color_continuous_midpoint=None, opacity=None, size_max=None, zoom=8)
