from keras.models import Sequential
from keras.layers import DepthwiseConv2D
model = Sequential()
model.add(DepthwiseConv2D((3, 3),  (1, 1),  'valid',  1,  None,  None,  True,  'glorot_uniform',  'zeros',  None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, bias_constraint=None))
