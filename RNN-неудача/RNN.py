from __future__ import absolute_import, division, print_function, unicode_literals
import keras
import collections
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from keras import layers


model = keras.Sequential()
# Добавим слой Embedding ожидая на входе словарь размера 1000, и
# на выходе вложение размерностью 64.
model.add(layers.Embedding(input_dim=1000, output_dim=64))

# Добавим слой LSTM с 128 внутренними узлами.
model.add(layers.LSTM(128))

# Добавим слой Dense с 10 узлами и активацией softmax.
model.add(layers.Dense(10))

model.summary()

model = keras.Sequential()
model.add(layers.Embedding(input_dim=1000, output_dim=64))

# Выходом GRU будет 3D тензор размера (batch_size, timesteps, 256)
model.add(layers.GRU(256, return_sequences=True))

# Выходом SimpleRNN будет 2D тензор размера (batch_size, 128)
model.add(layers.SimpleRNN(128))

model.add(layers.Dense(10))

model.summary()
