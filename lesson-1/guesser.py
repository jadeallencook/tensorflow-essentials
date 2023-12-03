# importing necessary libraries
import tensorflow as tf
import numpy as np
from tensorflow import keras

layers = keras.layers.Dense(units=1, input_shape=[1], kernel_initializer='random_normal')
optimizer = tf.keras.optimizers.legacy.SGD(learning_rate=0.001)
model = tf.keras.Sequential([layers])
model.compile(optimizer=optimizer, loss='mean_squared_error')

# get 5 numbers from user and store them in an array
xs = np.array(input("Enter 10 numbers: ").split(), dtype=int)

# get answers to all 5 numbers from user and store them in an array in a loop
ys = []
for i in range(10):
    ys.append(int(input("Enter answer to " + str(xs[i]) + ": ")))
ys = np.array(ys, dtype=int)

verbosity = 0
model.fit(xs, ys, epochs=8, verbose=verbosity)

# get user input for number to predict
prediction = model.predict([int(input("Enter number to predict: "))], verbose=verbosity)

# print prediction
print("\nPrediction: ", round(prediction[0][0]))
