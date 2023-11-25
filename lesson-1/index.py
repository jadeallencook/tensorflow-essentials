# importing necessary libraries
import tensorflow as tf
import numpy as np
from tensorflow import keras

# this is a Dense layer, a fundamental type of layer used in neural networks
# in a dense layer, every input is connected to every output by a weight

# units=1 means that there is only one output
# input_shape=[1] means that there is only one input
# kernel_initializer='random_normal' means that the weights are initialized randomly
layers = keras.layers.Dense(units=1, input_shape=[1], kernel_initializer='random_normal')

# this is the optimizer, which is used to minimize the loss function
# learning_rate=0.001 means that the optimizer will change the weights by 0.001
optimizer = tf.keras.optimizers.legacy.SGD(learning_rate=0.001)

# this is the model, which is a collection of layers
# the model is compiled with the optimizer and loss function
model = tf.keras.Sequential([layers])

# compiling the model
# optimizer=optimizer means that the model will use the optimizer
# loss='mean_squared_error' means that the loss function is the mean squared error

#  the loss function measures how well the model is performing
# i.e., how close the model's predictions are to the actual values
# and is used to guide the optimization of the model's weights
# mean_squared_error is one of the most common loss functions used in regression tasks
model.compile(optimizer=optimizer, loss='mean_squared_error')

# preparing data for training
# xs = [1, 2, 3, 4, 5, 6, ...]
# ys = [2, 4, 6, 8, 10, 12, ...]
xs = np.array(np.arange(50), dtype=int)
ys = np.array(xs * 2, dtype=int)

verbosity = 0
model.fit(xs, ys, epochs=8, verbose=verbosity)

# making predictions
prediction1 = model.predict([10], verbose=verbosity)
prediction1 = round(prediction1[0][0])
prediction2 = model.predict([3], verbose=verbosity)
prediction2 = round(prediction2[0][0])
prediction3 = model.predict([50], verbose=verbosity)
prediction3 = round(prediction3[0][0])
prediction4 = model.predict([125], verbose=verbosity)
prediction4 = round(prediction4[0][0])

# printing predictions
print("\nPrediction for 10 should be 20: ", prediction1)
print("Prediction for 3 should be 6: ", prediction2)
print("Prediction for 50 should be 100: ", prediction3)
print("Prediction for 125 should be 250: ", prediction4)
