import tensorflow as tf
model = tf.keras.Sequential([tf.keras.layers.Dense(5, input_shape=(3,)), tf.keras.layers.Softmax()])
model.save('output',  True,  True,  None, signatures=None)
