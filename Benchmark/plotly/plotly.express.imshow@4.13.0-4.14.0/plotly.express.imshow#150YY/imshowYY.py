import plotly.express as px
import numpy as np
img_rgb = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]], [[0, 255, 0], [0, 0, 255], [255, 0, 0]]], dtype=np.uint8)
fig = px.imshow(img_rgb,  None, zmax=None, origin=None, labels={}, x=None, y=None, color_continuous_scale=None, color_continuous_midpoint=None, range_color=None, title=None, template=None, width=None, height=None, aspect=None, contrast_rescaling=None)
