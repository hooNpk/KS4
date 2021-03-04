from keras.models import Sequential
from keras.layers import LSTM, Dense
import psycopg2 as pg2
import numpy as np
import matplotlib.pyplot as plt

conn = pg2.connect(database='postgres', user='postgres', password='secret', host='127.0.0.1')
cur = conn.cursor()
cur.execute('SELECT price, diff, diff_per, volume, gigwan, foreigner FROM test1;')
rows = cur.fetchall()
cur.close()
print(len(rows))

stride = 10
Y_test = np.array([rows[x][0] for x in range(10)])
X_test = np.array([rows[x+1:x+1+stride] for x in range(10)])
Y_train = np.array([rows[x][0] for x in range(11, len(rows)-stride)])
X_train = np.array([rows[x+1:x+1+stride] for x in range(11, len(rows)-stride)])
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

model = Sequential()
model.add(LSTM(units=16, input_shape=(X_train.shape[1], X_train.shape[2]), activation='relu', return_sequences=False))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')
print(model.summary())

EPOCHS = 10
history = model.fit(X_train, Y_train, epochs=EPOCHS, batch_size=10)
plt.plot(history.history['loss'])
plt.ylabel('loss')
plt.xlabel('epochs')
plt.show()