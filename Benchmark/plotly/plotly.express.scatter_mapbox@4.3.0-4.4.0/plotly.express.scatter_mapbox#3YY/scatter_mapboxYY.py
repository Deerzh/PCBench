import plotly.express as px
df = px.data.carshare()
fig = px.scatter_mapbox(df, lat='centroid_lat', lon='centroid_lon')
