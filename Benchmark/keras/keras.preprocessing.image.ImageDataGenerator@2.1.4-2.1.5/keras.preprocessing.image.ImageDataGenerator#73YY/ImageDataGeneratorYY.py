from keras.preprocessing.image import ImageDataGenerator
data_generator = ImageDataGenerator(False,  False,  False,  False,  False, zca_epsilon=1e-06, rotation_range=0.0, width_shift_range=0.0, height_shift_range=0.0, shear_range=0.0, zoom_range=0.0)
