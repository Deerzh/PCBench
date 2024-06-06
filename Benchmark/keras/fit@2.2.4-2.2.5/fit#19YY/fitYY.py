from keras.models import Sequential
from keras.layers import Dense
import numpy as np
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=20))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
x_train = np.random.random((1000, 20))
y_train = np.random.randint(2, size=(1000, 1))
model.fit(x_train,  y_train,  32,  1,  1,  None)
