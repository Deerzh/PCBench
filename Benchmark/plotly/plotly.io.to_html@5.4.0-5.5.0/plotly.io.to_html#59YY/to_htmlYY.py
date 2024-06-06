import plotly.graph_objects as go
import plotly.io as pio
fig = go.Figure(data=[go.Bar(y=[2, 3, 1])], layout_title_text='A Bar Chart')
html_string = pio.to_html(fig,  None,  True,  True,  False,  None, full_html=True, animation_opts=None, default_width='100%', default_height='100%')
