import numpy as np
import keras
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Activation, Embedding
from keras.layers import LSTM
from keras.datasets import imdb
import tensorflow as tf

# Устанавливаем seed для обеспечения повторяемости результатов
np.random.seed(42)

# Указываем количество слов из частотного словаря, которое будет использоваться (отсортированы по частоте использования)
max_features = 5000

# Загружаем данные (датасет IMDB содержит 25000 рецензий на фильмы с правильным ответом для обучения и 25000 рецензий на фильмы с правильным ответом для тестирования)
(X_train, y_train), (X_test, y_test) = imdb.load_data(nb_words=max_features)

# Устанавливаем максимальную длину рецензий в словах, чтобы они все были одной длины
maxlen = 80

X_train = sequence.pad_sequences(X_train, maxlen=maxlen)
X_test = sequence.pad_sequences(X_test, maxlen=maxlen)

# Создаем модель последовательной сети
model = Sequential()
# Добавляем слой для векторного представления слов (5000 слов, каждое представлено вектором из 32 чисел, отключаем входной сигнал с вероятностью 20% для предотвращения переобучения)
model.add(Embedding(max_features, 32))
# Добавляем слой долго-краткосрочной памяти (100 элементов для долговременного хранения информации, отключаем входной сигнал с вероятностью 20%, отключаем рекуррентный сигнал с вероятностью 20%)
model.add(LSTM(100, dropout=0.2))
# Добавляем полносвязный слой из 1 элемента для классификации, в качестве функции активации будем использовать сигмоидальную функцию
model.add(Dense(1, activation='sigmoid'))

# Компилируем модель нейронной сети
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Обучаем нейронную сеть (данные для обучения, ответы к данным для обучения, количество рецензий после анализа которого будут изменены веса, число эпох обучения, тестовые данные, показывать progress bar или нет)
model.fit(X_train, y_train,
          batch_size=64,
          epochs=9,
          validation_data=(X_test, y_test),
          verbose=1)

scores = model.evaluate(X_test, y_test, batch_size=64)
print('Точность на тестовых данных: %.2f%%' % (scores[1] * 100))

train_ds = keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)