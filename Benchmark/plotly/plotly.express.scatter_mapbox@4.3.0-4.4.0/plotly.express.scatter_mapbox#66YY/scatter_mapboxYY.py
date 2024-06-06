import plotly.express as px
df = px.data.carshare()
fig = px.scatter_mapbox(df,  'centroid_lat',  'centroid_lon',  'peak_hour',  None,  None, hover_data=None, custom_data=None, size=None, animation_frame=None, animation_group=None)
