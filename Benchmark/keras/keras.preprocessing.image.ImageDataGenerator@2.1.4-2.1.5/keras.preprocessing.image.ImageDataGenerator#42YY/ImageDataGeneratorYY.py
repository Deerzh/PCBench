from keras.preprocessing.image import ImageDataGenerator
data_generator = ImageDataGenerator(False,  False,  False, samplewise_std_normalization=False, zca_whitening=False, zca_epsilon=1e-06, rotation_range=0.0, width_shift_range=0.0)
