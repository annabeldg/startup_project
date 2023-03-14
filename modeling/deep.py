import pandas as pd
import os

from sklearn.model_selection import train_test_split

from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras.metrics import Precision
from tensorflow.keras.callbacks import EarlyStopping

data_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())),'startup_project')
data = pd.read_csv(os.path.join(data_path,'raw_data/startups_modified.csv'))

X = data.drop(columns='Target')
y = data['Target']

es = EarlyStopping(patience=3)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2)

model = Sequential()
model.add(layers.Dense(100, activation='relu', input_dim=len(X.columns)))
model.add(layers.Dense(100, activation='relu'))
model.add(layers.Dense(50, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

print(model.summary())


model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy', Precision()]
)

model.fit(X_train, y_train, batch_size=64, validation_split=0.3, epochs=20, callbacks=[es], verbose=1)

model.evaluate(X_test, y_test)
