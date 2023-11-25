# importing necessary libraries
import tensorflow as tf
import numpy as np
from tensorflow import keras

# setting up the neural network model
model = tf.keras.Sequential([keras.layers.Dense(
    units=1, input_shape=[1], kernel_initializer='random_normal')])
model.compile(optimizer=tf.keras.optimizers.legacy.SGD(
    learning_rate=0.001), loss='mean_squared_error')

# preparing data for training
xs = np.array(np.arange(50), dtype=int)
ys = np.array(xs * 2, dtype=int)

# xs = [1, 2, 3, 4, 5, 6, ...]
# ys = [2, 4, 6, 8, 10, 12, ...]

model.fit(xs, ys, epochs=8, verbose=0)

# making predictions
prediction1 = model.predict([10], verbose=0)
prediction1 = round(prediction1[0][0])
prediction2 = model.predict([3], verbose=0)
prediction2 = round(prediction2[0][0])
prediction3 = model.predict([50], verbose=0)
prediction3 = round(prediction3[0][0])
prediction4 = model.predict([125], verbose=0)
prediction4 = round(prediction4[0][0])

# printing predictions
print("\nPrediction for 10 should be 20: ", prediction1)
print("Prediction for 3 should be 6: ", prediction2)
print("Prediction for 50 should be 100: ", prediction3)
print("Prediction for 125 should be 250: ", prediction4)
