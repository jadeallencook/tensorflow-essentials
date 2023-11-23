import tensorflow as tf

import numpy as np

from tensorflow import keras

verbosity = 0

model = tf.keras.Sequential([keras.layers.Dense(
    units=1, input_shape=[1], kernel_initializer='random_normal')])

model.compile(optimizer=tf.keras.optimizers.SGD(
    learning_rate=0.001), loss='mean_squared_error')

xs = np.array(np.arange(50), dtype=int)
ys = np.array(xs * 2, dtype=int)
model.fit(xs, ys, epochs=8, verbose=verbosity)

prediction1 = model.predict([10], verbose=verbosity)
prediction2 = model.predict([3], verbose=verbosity)
prediction3 = model.predict([50], verbose=verbosity)
prediction4 = model.predict([125], verbose=verbosity)

print("Prediction for 10 should be 20: ", prediction1)
print("Prediction for 3 should be 6: ", prediction2)
print("Prediction for 50 should be 100: ", prediction3)
print("Prediction for 125 should be 250: ", prediction4)