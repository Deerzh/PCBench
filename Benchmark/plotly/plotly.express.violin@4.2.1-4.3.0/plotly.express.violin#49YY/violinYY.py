import plotly.express as px
df = px.data.tips()
fig = px.violin(df,  None,  'total_bill',  None,  None,  None, hover_name=None, hover_data=None, custom_data=None)
