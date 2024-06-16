from keras.models import Sequential # type: ignore
from keras.layers import ConvLSTM2D, BatchNormalization, Conv2D, Dense, Input, Dropout, GaussianNoise, MaxPooling2D # type: ignore
from loader import DataLoader
from sklearn.model_selection import train_test_split
from keras.callbacks import EarlyStopping
from keras.regularizers import L1
dl = DataLoader()
batch_len = 25
epochs_ = 3 # 80
X, y = dl.load_data(batch_len)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

model = Sequential()
model.add(Input(shape=(batch_len, 90, 180, 1)))


model.add(ConvLSTM2D(filters=32, kernel_size=(3, 3), padding='same', return_sequences=True,  kernel_regularizer=L1(0.001)))
model.add(Dropout(0.1))
model.add(BatchNormalization())
model.add(ConvLSTM2D(filters=32, kernel_size=(3, 3), padding='same', return_sequences=False,  kernel_regularizer=L1(0.001)))

model.add(BatchNormalization())
model.add(Dropout(0.1))

model.add(Conv2D(filters=1, kernel_size=(1, 1), activation='linear', padding='same',data_format ="channels_last", kernel_regularizer=L1(0.001)))


model.compile(optimizer='adam', loss='mse',metrics = ['mse','mae'])

early_stopping = EarlyStopping(monitor='val_loss', patience=5, mode='min', verbose=1, restore_best_weights = True,start_from_epoch =10)
model.summary()
model.fit(X_train, y_train, epochs=epochs_, batch_size=8, validation_split=0.2, callbacks = [early_stopping])

model.save("model.keras")

model.summary()
model.evaluate(X_test, y_test)