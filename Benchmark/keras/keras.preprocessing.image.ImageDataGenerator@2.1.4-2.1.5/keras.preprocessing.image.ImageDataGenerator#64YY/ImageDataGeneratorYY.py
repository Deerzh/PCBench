from keras.preprocessing.image import ImageDataGenerator
data_generator = ImageDataGenerator(False,  False, featurewise_std_normalization=False, samplewise_std_normalization=False, zca_whitening=False, zca_epsilon=1e-06, rotation_range=0.0, width_shift_range=0.0, height_shift_range=0.0, shear_range=0.0)
