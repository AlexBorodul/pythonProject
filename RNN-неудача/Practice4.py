import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense, Embedding

# Пример данных для обучения
nominative_cases = ['школа', 'больница', 'университет']
genitive_cases = ['школы', 'больницы', 'университета']

# Предобработка данных
input_data = np.array([nominative_cases])
output_data = np.array([genitive_cases])

# Создание модели нейронной сети
model = Sequential()
model.add(Embedding(input_dim=10000, output_dim=32, input_length=3))  # Предположим, что у нас есть векторное представление слов
model.add(LSTM(32))
model.add(Dense(3, activation='softmax'))  # 3 - количество падежей

# Компиляция модели
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# Обучение модели
model.fit(input_data, output_data, epochs=10, batch_size=32)

# Пример использования обученной модели
test_word = np.array([['школа']])
predicted_case = model.predict(test_word)
print(predicted_case)