import plotly.express as px
df = px.data.tips()
fig = px.density_contour(data_frame=df)
