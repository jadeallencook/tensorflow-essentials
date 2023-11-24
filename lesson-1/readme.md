# TensorFlow Basic Neural Network Tutorial

Welcome to this introductory tutorial on neural networks using TensorFlow! This README explains a simple Python script that demonstrates the basics of creating and training a neural network with TensorFlow, a powerful tool for machine learning.

## Script Overview

The provided script is a basic example of a machine learning model in TensorFlow. It's designed to introduce the fundamental concepts of neural networks and TensorFlow operations.

### Prerequisites

- Basic understanding of Python.
- TensorFlow installed in your environment.

### Importing Necessary Libraries

```python
import tensorflow as tf
import numpy as np
from tensorflow import keras
```

- **TensorFlow (tf):** The main library used for machine learning.
- **NumPy (np):** A library for numerical operations, used here for data array manipulation.
- **Keras:** A TensorFlow module that simplifies building neural networks.

### Setting up the Neural Network Model

```python
verbosity = 0
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1], kernel_initializer='random_normal')])
model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.001), loss='mean_squared_error')
```

- **Model Configuration:** Creates a sequential model with a single densely-connected neural layer.
- **Compilation:** Prepares the model for training, specifying the optimizer and loss function.

### Preparing Data for Training

```python
xs = np.array(np.arange(50), dtype=int)
ys = np.array(xs * 2, dtype=int)
model.fit(xs, ys, epochs=8, verbose=verbosity)
```

- **Data Arrays (xs, ys):** 'xs' is the input, and 'ys' is the expected output. In this case, 'ys' is double the 'xs'.
- **Model Training:** The fit method trains the model for a specified number of epochs.

### Making Predictions

```python
prediction1 = model.predict([10], verbose=verbosity)
prediction2 = model.predict([3], verbose=verbosity)
prediction3 = model.predict([50], verbose=verbosity)
prediction4 = model.predict([125], verbose=verbosity)

print("Prediction for 10 should be 20: ", prediction1)
print("Prediction for 3 should be 6: ", prediction2)
print("Prediction for 50 should be 100: ", prediction3)
print("Prediction for 125 should be 250: ", prediction4)
```

- **Model Predictions:** Using the predict method to test the trained model.
- **Output:** Displays the model's predictions for given inputs.

## Conclusion

This script is a basic introduction to building and training a neural network using TensorFlow. It covers key concepts such as model creation, data preparation, training, and making predictions. This foundational knowledge is crucial for delving deeper into machine learning and neural network applications.
